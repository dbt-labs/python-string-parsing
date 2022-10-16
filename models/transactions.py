import dateutil


def try_dateutil_parse(x):
    try:
        return dateutil.parser.parse(x)
    except:
        return


def model(dbt, session):
    df = dbt.ref("source_data")

    df['parsed_transaction_time'] = df['transaction_time'].apply(try_dateutil_parse)

    return df
