import weaviate
import logging

LOGGING_BATCH_SIZE = 30


def create_schema_word(client: weaviate.Client) -> None:
    word_class_schema = {
        "class": "Word",
        "description": "An english word",
        "vectorIndexConfig": {
            "distance": "cosine",
        },
        "properties": [
            {
                "name": "value",
                "dataType": ["string"],
                "description": "The word itself",
            },
        ]
    }
    client.schema.create_class(word_class_schema)


def seed_database_with_word(client: weaviate.Client) -> None:
    logging_batch_infos = []
    with open("./data/english_word_data.txt", "r") as f:
        for line in f.readlines():
            word = {
                'value': line.replace("\n", ""),
            }
            result = client.data_object.validate(
                data_object=word,
                class_name='Word',
            )
            if not result:
                print(f"Object Word {word.get('value')} not been validated, skipping...")
                continue
            client.data_object.create(
                data_object=word,
                class_name='Word',
            )
            if len(logging_batch_infos) < LOGGING_BATCH_SIZE:
                logging_batch_infos.append(word.get("value"))
            else:
                print(f"{len(logging_batch_infos)} word has been added -> {logging_batch_infos}")
                logging_batch_infos = []


if __name__ == "__main__":
    client = weaviate.Client("http://localhost:8080")
    print("Deleting all the current schema...")
    client.schema.delete_all()
    print("\n\n--------------------\n\n")
    print("Creating the word schema")
    create_schema_word(client)
    print("Done with the creation of the word shema")
    print("\n\n--------------------\n\n")
    print("Start populate the DataBase with word")
    seed_database_with_word(client)
    print("Done with the seeding of the DB")


