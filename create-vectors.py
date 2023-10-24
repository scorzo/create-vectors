import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions

def text_to_embedding(text, model):
    # use model to convert text to embeddings
    # For simplicity, this is a dummy function.
    return [1.0, 2.0, 3.0]  # Dummy embedding

def process(element):
    text = element
    embedding = text_to_embedding(text, None)  # Replace None with model
    return embedding

def run(argv=None, save_main_session=True):
    pipeline_options = PipelineOptions()
    pipeline_options.view_as(SetupOptions).save_main_session = save_main_session

    with beam.Pipeline(options=pipeline_options) as p:
        result = (
                p
                | 'Add Text' >> beam.Create(["likes Tacos on Tuesdays"])
                | 'Convert to Embedding' >> beam.Map(process)
                # Here you'd typically write the embedding to some storage
                | 'Write to BigQuery' >> WriteToBigQuery(
            'YOUR_PROJECT_ID:YOUR_DATASET.YOUR_TABLE',
            schema='field1:STRING, field2:INT64',  # Define your schema
            create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
            write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE
        )
        )

if __name__ == '__main__':
    run()
