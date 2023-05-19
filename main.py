import weaviate
from flask import Flask
from typing import Union

app = Flask(__name__)


def get_formated_db_response(response: dict, schema_name: str) -> list[Union[str, None]]:
    items_list = response.get("data", {}).get("Get", {}).get(schema_name)
    if not items_list:
        return []
    return {item.get("value"): item.get("_additional", {}).get("distance") for item in items_list}


def get_word_similarity(input_word: str, thresold: float = 1.0, limit: int = 3) -> list[str]:
    client = weaviate.Client("http://localhost:8080")
    response = (
        client.query
        .get("Word", ["value"])
        .with_near_text({
            "concepts": [input_word],
            "distance": thresold
        })
        .with_offset(1)
        .with_limit(limit)
        .with_offset(1)
        .with_additional(["distance"]).do()
    )

    return get_formated_db_response(response, "Word")


@app.route('/similarity/<word>', strict_slashes=False)
def word_similarity_endpoint(word):
    return get_word_similarity(word)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5050')


