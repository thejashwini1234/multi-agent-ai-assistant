from agents.retrieval_agent import retrieval_agent
from agents.validation_agent import validate_response

def manager_agent(user_query, vectorstore):

    response = retrieval_agent(
        vectorstore,
        user_query
    )

    validation = validate_response(response)

    return {
        "response": response,
        "validation": validation
    }