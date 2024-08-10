# Adwiro 2022
# Get billboard source data

class GetPrijemOverviewDataQuery:

    @staticmethod
    def query_prijem_overveiew_data():
        prijem_overveiew_data = f'''
                        select pk_prijem_overveiew_id, fk_prijem_overveiew_id, celkem_prijem 
                        from prijem_overview;'''
        return prijem_overveiew_data
