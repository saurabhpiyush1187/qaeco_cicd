import requests

class RequestBuilder:

    """
    Description:
        |  This class provides methods to build a URI using base_url, path params and query params.
        |  This class allows user to modify path params and query params existing in an URI
        |  This class also let's user call a web service request.

    """


    def call_request(self, pstr_method, pstr_url, pdict_headers, **kwargs):
        """
        Description:
            |  This method allows user to call a Get/Post/Put/Post/Patch/Delete request

        :param pstr_method: Type of request. Get or Post etc..
        :type pstr_method: String
        :param pstr_url: Request URL
        :type pstr_url: String
        :param pdict_headers: Headers to call a request
        :type pdict_headers: dictionary
        :param pstr_payload: payload dictionary
        :type pstr_payload: dictionary
        :param pbln_allow_redirects:
        :type pbln_allow_redirects: boolean
        :param pbln_verify:
        :type pbln_verify: boolean

        :return: response - response generated on calling a request
        .. code-block:: python

            call_request(“Get”,”https://www.samplesite.com/param1/param2”,headers={“Accept”:”application/json”})
            call_request(“Post”,”https://www.samplesite.com/param1/param2”,headers={“Accept”:”application/json”},pstr_payload=’{“KOU”:”123456”}’)

        .. note::
            |  pstr_method (String) :
            |  Accepts: Get, Post,Put, Patch or Delete
            |  Correct: get/GET/Get
            |  Wrong: gEt/GEt
            |
            |
            |  Default Values for Kwargs:
            |  2. Default value of **kwargs parameter pstr_payload is None
            |  4. Default value of **kwargs parameter pbln_allow_redirects is False
            |  6. Default value of **kwargs parameter pbln_verify is False

        """
        try:
            response=''
            if pstr_url == "":
                return None
            pstr_payload = kwargs.get('pstr_payload', None)
            pbln_allow_redirects = kwargs.get('pbln_allow_redirects', False)
            pbln_verify = kwargs.get('pbln_verify', False)


            if pstr_method.islower() or pstr_method.isupper() or pstr_method.istitle():

                if pstr_method.capitalize() == "Get":
                    response = requests.get(pstr_url,
                                            headers=pdict_headers,
                                            verify=pbln_verify,
                                            allow_redirects=pbln_allow_redirects,
                                            data=pstr_payload
                                            )
                elif pstr_method.capitalize() == "Post":
                    if pstr_payload is not None:
                        response = requests.post(pstr_url,
                                                 headers=pdict_headers,
                                                 data=pstr_payload,
                                                 verify=pbln_verify,
                                                 allow_redirects=pbln_allow_redirects
                                                 )
                    else:
                        raise Exception("Error-->Payload is missing")
                elif pstr_method.capitalize() == "Put":
                    if pstr_payload is not None:
                        response = requests.put(pstr_url,
                                                headers=pdict_headers,
                                                data=pstr_payload,
                                                verify=pbln_verify,
                                                allow_redirects=pbln_allow_redirects
                                                )
                    else:
                        raise Exception("Error-->Payload is missing")
                elif pstr_method.capitalize() == "Patch":
                    if pstr_payload is not None:
                        response = requests.patch(pstr_url,
                                                  headers=pdict_headers,
                                                  data=pstr_payload,
                                                  verify=pbln_verify,
                                                  allow_redirects=pbln_allow_redirects
                                                  )
                    else:
                        raise Exception("Error-->Payload is missing")
                else:
                    if pstr_method.capitalize() == "Delete":
                        response = requests.delete(pstr_url,
                                                   headers=pdict_headers,
                                                   verify=pbln_verify,
                                                   allow_redirects=pbln_allow_redirects,
                                                   data=pstr_payload
                                                   )

                return response
            else:
                raise Exception('Error-->The parameter pstr_method can only be lowercase/uppercase/camelcase '
                                'i.e, get/GET/Get and not something like gEt/GEt etc')
        except Exception as e:
                print(e)



    def get_response_statuscode(self, pobj_response_obj):
        """
        Description:
            |  This method returns status code of the response that is passed

        :param pobj_response_obj: Response object whose status code is needed
        :type pobj_response_obj: Object

        :return: status code integer
        """
        try:
            if pobj_response_obj is None:
                return None
            else:
                return pobj_response_obj.status_code
        except Exception as e:
            print(e)
