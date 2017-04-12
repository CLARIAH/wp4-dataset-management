# wp4-dataset-management
### Simple web app for generating SPARQL queries for removing older versions of datasets

### What it does

* The app queries the datalegend SPARQL endpoint to retrieve all dataset definitions (nanopublications).
* It renders a web page, where users can toggle candidate dataset versions for deletion
* At the bottom of the page, clicking the button `Generate SPARQL query` will generate the SPARQL query/queries needed to delete the corresponding graphs from the triplestore
* This query can only be executed through an endpoint with the proper access rights (copy & paste)
* **NB:** the web app does not allow the direct execution of the query.

### Starting

* Initiate and activate a `virtualenv` if you so desire
* Run `pip install requirements.txt`
* **Optional**: Set the `ENDPOINT` variable in `src/app/config.py` to point to the proper SPARQL endpoint
* Change dir into `src`
* Run `python run.py`
* The application will be running at <http://localhost:5000>
