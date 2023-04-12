def secret_authentication(secret, credits):
    """
    Checks whether a valid secret-key is received and, 
    if so, verifies whether the user has enough credits 
    to perform the requested action. If the user has 
    enough credits, the function subtracts the credits 
    consumed by the request from the user's credit balance.

    Parameters:
        secret (str)
            The secret-key received in request
        credits (double)
            The number of credits consumed by the specific 
            request

    Returns:
        Raises an error if the user does not have enough 
        credits or if the secret-key is incorrect. Otherwise, 
        it does not return anything.
    """
    pass