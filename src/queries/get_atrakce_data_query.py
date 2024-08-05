# Adwiro 2022
# Get billboard source data

class GetAtrakceDataQuery:

    @staticmethod
    def query_atrakce_data():
        atrakce_data = f''' select pk_atrakce_id, atrakce_nazev from atrakce_dict;
                 ;'''
        return atrakce_data
