from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from movie_locations.models import Movie
from . import tweet
from . import wiki
from django.core import serializers


def movie_locations(request):
    '''
        Variables:
        user_input (str) = movie name

        Return value:
        Return narrative location of the user_input and current Twitter trends for its nearest location.
    '''
    try:
        # Get narrative location from mySQL database. This data is sourced from Wiki https://query.wikidata.org/sparql
        user_input = request.GET.get('q', '')
    except:
        return JsonResponse({"status_code": 400, "status": "Bad Request",
                             "message": "Please submit a valid request."})
    else:
        try:
            #First try to get exact match.
            movie_locations = Movie.objects.filter(movie_name__iexact=user_input.lower()).order_by("id")
            #If there is no exact match and user_input contains string, get closest match.
            if len(movie_locations) < 1 and len(user_input.strip())>0:
                movie_locations = Movie.objects.filter(movie_name__icontains=user_input.lower())

            # Get the first result that matches the query
            movie_obj = movie_locations[0]
        except:
            return JsonResponse({"status_code": 404, "status": "Not Found",
                                 "message": "Not found. Please enter another movie name in your query."})
        else:

            # Create dictionary for movie details to be returned
            return_value = {"MovieDetails":
                            {"MovieName": movie_obj.movie_name,
                             "Movielink": movie_obj.movie_link,
                             "Coordinates": movie_obj.coordinates,
                             "NarrativeLocation": movie_obj.narrative_location}
                            }

            # The coordinates come in this format: Point (long lat)
            movie_format = movie_obj.coordinates.replace('Point', '').replace(')', '').replace('(', '').strip()
            #movie_format = movie_coord_full
            movie_coord = movie_format.split()

            # Get trends for nearest location in Twitter.
            my_trend = tweet.Trends()
            my_api = my_trend.set_tweep_connection()

            return_value["TwitterTrends"] = my_trend.get_location_trends(my_api, movie_coord[1], movie_coord[0])
            return JsonResponse(return_value, safe=False)


def movie_load(request):
    '''
        Full delete and load Movie model from WikiApp.
    '''
    if request.method == "POST":
        my_app = wiki.WikiApp()
        my_message = my_app.load_movie_data()
        return JsonResponse({"status_code": 202, "status": "Accepted",
                             "message": my_message})
    return JsonResponse({"status_code": 400, "status": "Bad Request",
                         "message": "Please submit a valid request."})
