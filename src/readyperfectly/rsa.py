# API Lambdas
# ut_get_favicon_ico: Redirect to favicon.ico URL hosted on S3 (accessible via CloudFront CDN)

import logging
from jwcrypto.jwk import JWK

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# GET /rsa/key-pair
def get_rsa_key_pair(event:dict, context):
    """
    Generates RSA key pair using RS256 (RSA Signature with SHA-256) using 2048 bits for key size.
    Suitable for use with Json Web Token (JWT) and not JWE (JSON Web Encryption).

    Args:
        event (Dict): The API Gateway event object containing request details.
        context (object): The Lambda context object, which provides methods and
                          properties about the invocation, function, and execution environment.

    Returns:
        Dict: An API Gateway-compatible response dictionary with a 200 status code
              and the 'Location' header set to the favicon URL.

    """
    print("[event]", event)
    print("[context]", context)

    private_key = JWK.generate(kty='RSA', size=2048, alg='RS256', use='sig')
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
        },
        'body': private_key.export()
    }
