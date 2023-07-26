from bottle import route, run, request
from const import *
from openai_message import create_prompt_to_summarise_message, get_message

from typetalk import (
    set_typetalk_talkName,
    get_typetalk_talk,
    post_typetalk_message,
)


# Receive data from Typetalk.
@route("/", method="POST")
def handle_event():
    data = request.json

    # Debug
    print(f"data: {data}\n")

    user_message = data["post"]["message"]
    user_postid = data["post"]["id"]

    # まとめIDがある(会話が継続している場合)
    if len(data["post"]["talks"]):
        talk_id = data["post"]["talks"][0]["id"]

    # No talk ID ( The caase of new conversation. )
    # Summerise the message and create a Typetalk tag.
    # Receice the Talk ID.
    else:
        prompt = create_prompt_to_summarise_message(user_message)
        summarized_talkname_title = get_message(prompt)
        talk_id = set_typetalk_talkName(summarized_talkname_title, user_postid)

    # Sort conversation history in ascending order.
    sorted_result = get_typetalk_talk(talk_id)

    # Debug
    print(f"get_typetalk_talk: {sorted_result}\n")

    # Receive the OpenAI API response.
    return_message = get_message(sorted_result)

    # Debug
    print(f"return_message: {return_message}\n")

    # Post OpenAI API responses to the Typetalk topic.
    post_typetalk_message(return_message, user_postid, talk_id)


def main():
    print("Server Start")
    run(host="0.0.0.0", port=8080, debug=True, reloader=True)
    # run(host='0.0.0.0', port=8080, debug=False, reloader=False)


if __name__ == "__main__":
    main()
