import csv
from app.db import collection, embedding_model

def ingest_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        print("CSV columns:", reader.fieldnames)  # Debug print
        docs, metas, ids = [], [], []
        for row in reader:
            description = row.get("Summary")  # Use 'Summary' for description
            resolution = row.get("Latest Comments")  # Use 'Latest Comments' for resolution
            ticket_id = row.get("Ticket Number")
            if not description or not resolution:
                print(f"Skipping row due to missing fields: {row}")
                continue
            docs.append(description)
            metas.append({"resolution": resolution})
            ids.append(ticket_id if ticket_id else str(len(ids)))
        if docs:  # Only proceed if there is data to ingest
            embeddings = embedding_model.encode(docs).tolist()
            collection.add(documents=docs, metadatas=metas, ids=ids, embeddings=embeddings)
            print(f"Ingested {len(docs)} tickets.")
        else:
            print("No valid tickets to ingest.")

if __name__ == "__main__":
    ingest_csv("./data/incidents.csv")