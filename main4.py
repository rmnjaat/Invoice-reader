from mindee import Client, PredictResponse, product

# Init a new client
mindee_client = Client(api_key="apikey")

# Load a file from disk
input_doc = mindee_client.source_from_path("abc.pdf")

# Load a file from disk and parse it.
# The endpoint name must be specified since it cannot be determined from the class.
result: PredictResponse = mindee_client.parse(product.InvoiceV4, input_doc)

# Print a summary of the API result
# print(result.document)

# Print the document-level summary
print(result.document.inference.prediction)
