# Adwiro 2022
# Get billboard source data

class GetAttractionDataQuery:

    @staticmethod
    def query_attraction_data():
        attraction_data = f''' select pk_attraction_dictionary_id, attraction_name from ars_attraction_dictionary;'''
        return attraction_data
