# pip install sparqlwrapper
# https://rdflib.github.io/sparqlwrapper/

from SPARQLWrapper import SPARQLWrapper, JSON
from datetime import datetime
from movie_locations.models import Movie


class WikiApp:

    def load_movie_data(self):
        '''
            Truncates table according to table_name variable and re-populates from Wikidata source.
        '''
        sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
        sparql.setQuery("""#Movies and their narrative location on a map
        #defaultView:Map
        #removed: ?narrative_location
          #OPTIONAL { ?movie wdt:P577 ?publication_date. }
        SELECT ?movie ?movieLabel ?narrative_locationLabel ?coordinates WHERE {
           ?movie wdt:P840 ?narrative_location ;
                  wdt:P31 wd:Q11424 .
           ?narrative_location wdt:P625 ?coordinates .
          SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
        }""")

        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

        Movie.objects.all().delete()

        for result in results["results"]["bindings"]:
            movie_link = result["movie"]["value"]
            movie_label = result["movieLabel"]["value"]
            location_label = result["narrative_locationLabel"]["value"]
            coordinates = result["coordinates"]["value"]
            record = Movie(movie_link=movie_link, movie_name=movie_label, narrative_location=location_label, coordinates=coordinates)
            record.save()
        record_num = Movie.objects.count()
        return f"Inserted {record_num} records on {datetime.now()}."
