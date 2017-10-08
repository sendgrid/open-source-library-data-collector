"""
utils.py

Utility functions for working with data
"""
import csv


def write_records_to_csv(filepath, records, headers=None):
    """Write a list of lists to a CSV (comma separated values) file, where
       each sub-list is a row of data.

    :param filepath: Path to the file to write, including export name
    :type filepath:  basestring

    :param records: List of lists to put in CSV. Each sub-list is made of
                    things that can be written, like strings or numbers
    :type records:  list

    :param headers: List of column headers as strings. If not provided,
                    no header is written.
    :type headers: list
    """
    with open(filepath, 'w') as fp:
        writer = csv.writer(fp)
        if headers:
            writer.writerow(headers)
        writer.writerows(records)
