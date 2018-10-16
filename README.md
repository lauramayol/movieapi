# Project: Movie Locations API
*Release: 0.1*


This project provides a simple API to recieve a movie name, retrieve the narrative location and its current Twitter trends.

## Features

#### This release
- [x] Get narrative location for a given movie and its coordinates.
- [x] Get nearest location that Twitter is tracking.
- [x] Get top 10 Twitter trends.
- [x] Write api docs.
- [x] Checks partial matches if no exact entry is found

#### Next release

- [ ] Option to use filming location and select based on movie release year.


### Paths

| Location | Path |
| :-- | :-- |
| Root path | `~/`|
| Movie | `~/movie`|
| Load  | `~/movie/load`|

### HTTP request and query methods

| Method | Path | Query | Description | Examples |
| :-- | :-- | :-- | :-- | :-- |
| `GET` | `~/movie` | `?q=full%20name` | Retrieves the narrative location of a movie, nearest Twitter location and its current top 10 trends. | `~/movie?q=notting%20hill` |
| `POST` | `~/movie/load` | na | Loads latest movie data from Wikidata. Specfically, it truncates current SQL table, queries Wikidata for its latest movie details, and inserts all records into table. | `~~/movie/load` |

### Contribute

- Issue Tracker: https://github.com/lauramayol/movieapi/issues
- Source Code: https://github.com/lauramayol/movieapi


### Support


If you are having issues, please let me know.
