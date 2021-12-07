""" Run the following to test the scenario"""
import random
from concurrent.futures import ThreadPoolExecutor
from postgres_python_test.pg_test import DBConnector
from postgres_python_test.write_to_csv import write_to_csv

if "__main__":
    """
    To verify that postgres has no issue updating row concurrently as long as they are different row, 
    run the operation in the following order.
    
    1. create csv file and do bulk insert. For that uncomment write_to_csv and connector.bulk_insert method.
        This will insert million record
    2. Secondly, comment back both methods and just uncomment line 29 till line 35. This will randomly update paralley 2000 rows.
    
    3. Executing method of line 39 will give changes lists and we can run the test to verify if both lists are same. 
    """
    ######################################################################
    # uncomment to generate a csv file of 1 million records locally
    # write_to_csv()
    ######################################################################

    connector = DBConnector()
    ######################################################################
    # uncomment to do bulk insertion of 1 million record to postgres
    # connector.bulk_insert()
    ######################################################################
    # update test
    # rows_to_update = random.sample(range(0, 1000000), 2000)
    # print('########## rows to update#########')
    # print(rows_to_update)
    # print('##################################')
    # # parallel invocation block for update
    # with ThreadPoolExecutor() as executor:
    #     results = executor.map(connector.update, rows_to_update)

    ######################################################################
    # get all method to see data
    result = connector.get_all_changed_rows()
    print(result)

    ######################################################################
