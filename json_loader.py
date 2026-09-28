VAR = r"""{
    "reasoningEngines": [
        {
        "name": "projects/154372397551/locations/us-central1/reasoningEngines/2412545664887029760",
        "displayName": "Agente LeanIX - SapLeanIX Inventory",
        "spec": {
            "classMethods": [
            {
                "api_mode": "",
                "description": "Deprecated. Use async_get_session instead.\n\n        Get a session for the given user.\n        ",
                "name": "get_session",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id",
                    "session_id"
                ]
                }
            },
            {
                "api_mode": "",
                "description": "Deprecated. Use async_list_sessions instead.\n\n        List sessions for the given user.\n        ",
                "name": "list_sessions",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id"
                ]
                }
            },
            {
                "api_mode": "",
                "description": "Deprecated. Use async_create_session instead.\n\n        Creates a new session.\n        ",
                "name": "create_session",
                "parameters": {
                "type": "object",
                "properties": {
                    "ttl": {
                    "type": "string",
                    "nullable": true
                    },
                    "expire_time": {
                    "type": "string",
                    "nullable": true
                    },
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string",
                    "nullable": true
                    },
                    "state": {
                    "type": "object",
                    "nullable": true
                    }
                },
                "required": [
                    "user_id"
                ]
                }
            },
            {
                "api_mode": "",
                "description": "Deprecated. Use async_delete_session instead.\n\n        Deletes a session for the given user.\n        ",
                "name": "delete_session",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id",
                    "session_id"
                ]
                }
            },
            {
                "api_mode": "async",
                "description": "Get a session for the given user.\n\n        Args:\n            user_id (str):\n                Required. The ID of the user.\n            session_id (str):\n                Required. The ID of the session.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                session service.\n\n        Returns:\n            Session: The session instance (if any). It returns None if the\n            session is not found.\n\n        Raises:\n            RuntimeError: If the session is not found.\n        ",
                "name": "async_get_session",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id",
                    "session_id"
                ]
                }
            },
            {
                "api_mode": "async",
                "description": "List sessions for the given user.\n\n        Args:\n            user_id (str):\n                Required. The ID of the user.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                session service.\n\n        Returns:\n            ListSessionsResponse: The list of sessions.\n        ",
                "name": "async_list_sessions",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id"
                ]
                }
            },
            {
                "api_mode": "async",
                "description": "Creates a new session.\n\n        Args:\n            user_id (str):\n                Required. The ID of the user.\n            session_id (str):\n                Optional. The ID of the session. If not provided, an ID\n                will be generated for the session.\n            state (dict[str, Any]):\n                Optional. The initial state of the session.\n            ttl (str):\n                Optional. The time-to-live for the session.\n            expire_time (str):\n                Optional. The expiration time for the session.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                session service.\n\n        Returns:\n            Session: The newly created session instance.\n        ",
                "name": "async_create_session",
                "parameters": {
                "type": "object",
                "properties": {
                    "ttl": {
                    "type": "string",
                    "nullable": true
                    },
                    "expire_time": {
                    "type": "string",
                    "nullable": true
                    },
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string",
                    "nullable": true
                    },
                    "state": {
                    "type": "object",
                    "nullable": true
                    }
                },
                "required": [
                    "user_id"
                ]
                }
            },
            {
                "api_mode": "async",
                "description": "Deletes a session for the given user.\n\n        Args:\n            user_id (str):\n                Required. The ID of the user.\n            session_id (str):\n                Required. The ID of the session.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                session service.\n        ",
                "name": "async_delete_session",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id",
                    "session_id"
                ]
                }
            },
            {
                "api_mode": "async",
                "description": "Generates memories.\n\n        Args:\n            session (Dict[str, Any]):\n                Required. The session to use for generating memories. It should\n                be a dictionary representing an ADK Session object, e.g.\n                session.model_dump(mode=\"json\").\n        ",
                "name": "async_add_session_to_memory",
                "parameters": {
                "type": "object",
                "properties": {
                    "session": {
                    "type": "object",
                    "additionalProperties": true
                    }
                },
                "required": [
                    "session"
                ]
                }
            },
            {
                "api_mode": "async",
                "description": "Searches memories for the given user.\n\n        Args:\n            user_id: The id of the user.\n            query: The query to match the memories on.\n\n        Returns:\n            A SearchMemoryResponse containing the matching memories.\n        ",
                "name": "async_search_memory",
                "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                    "type": "string"
                    },
                    "user_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id",
                    "query"
                ]
                }
            },
            {
                "api_mode": "stream",
                "description": "Deprecated. Use async_stream_query instead.\n\n        Streams responses from the ADK application in response to a message.\n\n        Args:\n            message (Union[str, Dict[str, Any]]):\n                Required. The message to stream responses for.\n            user_id (str):\n                Required. The ID of the user.\n            session_id (str):\n                Optional. The ID of the session. If not provided, a new\n                session will be created for the user.\n            run_config (Optional[Dict[str, Any]]):\n                Optional. The run config to use for the query. If you want to\n                pass in a `run_config` pydantic object, you can pass in a dict\n                representing it as `run_config.model_dump(mode=\"json\")`.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                runner.\n\n        Yields:\n            The output of querying the ADK application.\n        ",
                "name": "stream_query",
                "parameters": {
                "type": "object",
                "properties": {
                    "run_config": {
                    "type": "object",
                    "nullable": true
                    },
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string",
                    "nullable": true
                    },
                    "message": {
                    "anyOf": [
                        {
                        "type": "string"
                        },
                        {
                        "type": "object",
                        "additionalProperties": true
                        }
                    ]
                    }
                },
                "required": [
                    "message",
                    "user_id"
                ]
                }
            },
            {
                "api_mode": "async_stream",
                "description": "Streams responses asynchronously from the ADK application.\n\n        Args:\n            message (str):\n                Required. The message to stream responses for.\n            user_id (str):\n                Required. The ID of the user.\n            session_id (str):\n                Optional. The ID of the session. If not provided, a new\n                session will be created for the user.\n            run_config (Optional[Dict[str, Any]]):\n                Optional. The run config to use for the query. If you want to\n                pass in a `run_config` pydantic object, you can pass in a dict\n                representing it as `run_config.model_dump(mode=\"json\")`.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                runner.\n\n        Yields:\n            Event dictionaries asynchronously.\n        ",
                "name": "async_stream_query",
                "parameters": {
                "type": "object",
                "properties": {
                    "run_config": {
                    "type": "object",
                    "nullable": true
                    },
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string",
                    "nullable": true
                    },
                    "message": {
                    "anyOf": [
                        {
                        "type": "string"
                        },
                        {
                        "type": "object",
                        "additionalProperties": true
                        }
                    ]
                    }
                },
                "required": [
                    "message",
                    "user_id"
                ]
                }
            },
            {
                "api_mode": "async_stream",
                "description": "Streams responses asynchronously from the ADK application.\n\n        In general, you should use `async_stream_query` instead, as it has a\n        more structured API and works with the respective ADK services that\n        you have defined for the AdkApp. This method is primarily meant for\n        invocation from AgentSpace.\n\n        Args:\n            request_json (str):\n                Required. The request to stream responses for.\n        ",
                "name": "streaming_agent_run_with_events",
                "parameters": {
                "type": "object",
                "properties": {
                    "request_json": {
                    "type": "string"
                    }
                },
                "required": [
                    "request_json"
                ]
                }
            }
            ],
            "deploymentSpec": {
            "env": [
                {
                "name": "LEANIX_API_TOKEN",
                "value": "LXT_PHXGT8CF5WgwUaVyfG5meyR5yhzv77cYOMthucYJ"
                },
                {
                "name": "LEANIX_BASE_URL",
                "value": "https://tma.leanix.net/"
                },
                {
                "name": "GCP_PROJECT_ID",
                "value": "tma-gemini-enterprise"
                },
                {
                "name": "GCP_REGION",
                "value": "us-central1"
                },
                {
                "name": "GOOGLE_CLOUD_LOCATION",
                "value": "us-central1"
                },
                {
                "name": "AGENT_ENGINE_RESOURCE_NAME",
                "value": "projects/154372397551/locations/us-central1/reasoningEngines/2412545664887029760"
                }
            ]
            },
            "agentFramework": "google-adk",
            "sourceCodeSpec": {
            "inlineSource": {},
            "imageSpec": {}
            },
            "effectiveIdentity": "service-154372397551@gcp-sa-aiplatform-re.iam.gserviceaccount.com"
        },
        "createTime": "2026-09-01T20:17:03.310028Z",
        "updateTime": "2026-09-21T16:20:01.158585Z",
        "description": "Agente especializado en consultas sobre el inventario de SapLeanIX (aplicaciones, iniciativas, componentes IT, fact sheets).",
        "contextSpec": {
            "memoryBankConfig": {
            "generationConfig": {}
            }
        }
        },
        {
        "name": "projects/154372397551/locations/us-central1/reasoningEngines/9070308473396264960",
        "displayName": "Tito Files Uploader",
        "spec": {
            "classMethods": [
            {
                "name": "get_session",
                "description": "Deprecated. Use async_get_session instead.\n\n        Get a session for the given user.\n        ",
                "api_mode": "",
                "parameters": {
                "required": [
                    "user_id",
                    "session_id"
                ],
                "type": "object",
                "properties": {
                    "session_id": {
                    "type": "string"
                    },
                    "user_id": {
                    "type": "string"
                    }
                }
                }
            },
            {
                "name": "list_sessions",
                "description": "Deprecated. Use async_list_sessions instead.\n\n        List sessions for the given user.\n        ",
                "api_mode": "",
                "parameters": {
                "required": [
                    "user_id"
                ],
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    }
                }
                }
            },
            {
                "name": "create_session",
                "description": "Deprecated. Use async_create_session instead.\n\n        Creates a new session.\n        ",
                "api_mode": "",
                "parameters": {
                "required": [
                    "user_id"
                ],
                "type": "object",
                "properties": {
                    "expire_time": {
                    "type": "string",
                    "nullable": true
                    },
                    "state": {
                    "type": "object",
                    "nullable": true
                    },
                    "session_id": {
                    "type": "string",
                    "nullable": true
                    },
                    "ttl": {
                    "type": "string",
                    "nullable": true
                    },
                    "user_id": {
                    "type": "string"
                    }
                }
                }
            },
            {
                "name": "delete_session",
                "description": "Deprecated. Use async_delete_session instead.\n\n        Deletes a session for the given user.\n        ",
                "api_mode": "",
                "parameters": {
                "required": [
                    "user_id",
                    "session_id"
                ],
                "type": "object",
                "properties": {
                    "session_id": {
                    "type": "string"
                    },
                    "user_id": {
                    "type": "string"
                    }
                }
                }
            },
            {
                "name": "async_get_session",
                "description": "Get a session for the given user.\n\n        Args:\n            user_id (str):\n                Required. The ID of the user.\n            session_id (str):\n                Required. The ID of the session.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                session service.\n\n        Returns:\n            Session: The session instance (if any). It returns None if the\n            session is not found.\n\n        Raises:\n            RuntimeError: If the session is not found.\n        ",
                "api_mode": "async",
                "parameters": {
                "required": [
                    "user_id",
                    "session_id"
                ],
                "type": "object",
                "properties": {
                    "session_id": {
                    "type": "string"
                    },
                    "user_id": {
                    "type": "string"
                    }
                }
                }
            },
            {
                "name": "async_list_sessions",
                "description": "List sessions for the given user.\n\n        Args:\n            user_id (str):\n                Required. The ID of the user.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                session service.\n\n        Returns:\n            ListSessionsResponse: The list of sessions.\n        ",
                "api_mode": "async",
                "parameters": {
                "required": [
                    "user_id"
                ],
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    }
                }
                }
            },
            {
                "name": "async_create_session",
                "description": "Creates a new session.\n\n        Args:\n            user_id (str):\n                Required. The ID of the user.\n            session_id (str):\n                Optional. The ID of the session. If not provided, an ID\n                will be generated for the session.\n            state (dict[str, Any]):\n                Optional. The initial state of the session.\n            ttl (str):\n                Optional. The time-to-live for the session.\n            expire_time (str):\n                Optional. The expiration time for the session.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                session service.\n\n        Returns:\n            Session: The newly created session instance.\n        ",
                "api_mode": "async",
                "parameters": {
                "required": [
                    "user_id"
                ],
                "type": "object",
                "properties": {
                    "expire_time": {
                    "type": "string",
                    "nullable": true
                    },
                    "state": {
                    "type": "object",
                    "nullable": true
                    },
                    "session_id": {
                    "type": "string",
                    "nullable": true
                    },
                    "ttl": {
                    "type": "string",
                    "nullable": true
                    },
                    "user_id": {
                    "type": "string"
                    }
                }
                }
            },
            {
                "name": "async_delete_session",
                "description": "Deletes a session for the given user.\n\n        Args:\n            user_id (str):\n                Required. The ID of the user.\n            session_id (str):\n                Required. The ID of the session.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                session service.\n        ",
                "api_mode": "async",
                "parameters": {
                "required": [
                    "user_id",
                    "session_id"
                ],
                "type": "object",
                "properties": {
                    "session_id": {
                    "type": "string"
                    },
                    "user_id": {
                    "type": "string"
                    }
                }
                }
            },
            {
                "name": "async_add_session_to_memory",
                "description": "Generates memories.\n\n        Args:\n            session (Dict[str, Any]):\n                Required. The session to use for generating memories. It should\n                be a dictionary representing an ADK Session object, e.g.\n                session.model_dump(mode=\"json\").\n        ",
                "api_mode": "async",
                "parameters": {
                "required": [
                    "session"
                ],
                "type": "object",
                "properties": {
                    "session": {
                    "additionalProperties": true,
                    "type": "object"
                    }
                }
                }
            },
            {
                "name": "async_search_memory",
                "description": "Searches memories for the given user.\n\n        Args:\n            user_id: The id of the user.\n            query: The query to match the memories on.\n\n        Returns:\n            A SearchMemoryResponse containing the matching memories.\n        ",
                "api_mode": "async",
                "parameters": {
                "required": [
                    "user_id",
                    "query"
                ],
                "type": "object",
                "properties": {
                    "query": {
                    "type": "string"
                    },
                    "user_id": {
                    "type": "string"
                    }
                }
                }
            },
            {
                "name": "stream_query",
                "description": "Deprecated. Use async_stream_query instead.\n\n        Streams responses from the ADK application in response to a message.\n\n        Args:\n            message (Union[str, Dict[str, Any]]):\n                Required. The message to stream responses for.\n            user_id (str):\n                Required. The ID of the user.\n            session_id (str):\n                Optional. The ID of the session. If not provided, a new\n                session will be created for the user.\n            run_config (Optional[Dict[str, Any]]):\n                Optional. The run config to use for the query. If you want to\n                pass in a `run_config` pydantic object, you can pass in a dict\n                representing it as `run_config.model_dump(mode=\"json\")`.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                runner.\n\n        Yields:\n            The output of querying the ADK application.\n        ",
                "api_mode": "stream",
                "parameters": {
                "required": [
                    "message",
                    "user_id"
                ],
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string",
                    "nullable": true
                    },
                    "run_config": {
                    "type": "object",
                    "nullable": true
                    },
                    "message": {
                    "anyOf": [
                        {
                        "type": "string"
                        },
                        {
                        "additionalProperties": true,
                        "type": "object"
                        }
                    ]
                    }
                }
                }
            },
            {
                "name": "async_stream_query",
                "description": "Streams responses asynchronously from the ADK application.\n\n        Args:\n            message (str):\n                Required. The message to stream responses for.\n            user_id (str):\n                Required. The ID of the user.\n            session_id (str):\n                Optional. The ID of the session. If not provided, a new\n                session will be created for the user.\n            run_config (Optional[Dict[str, Any]]):\n                Optional. The run config to use for the query. If you want to\n                pass in a `run_config` pydantic object, you can pass in a dict\n                representing it as `run_config.model_dump(mode=\"json\")`.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                runner.\n\n        Yields:\n            Event dictionaries asynchronously.\n        ",
                "api_mode": "async_stream",
                "parameters": {
                "required": [
                    "message",
                    "user_id"
                ],
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string",
                    "nullable": true
                    },
                    "run_config": {
                    "type": "object",
                    "nullable": true
                    },
                    "message": {
                    "anyOf": [
                        {
                        "type": "string"
                        },
                        {
                        "additionalProperties": true,
                        "type": "object"
                        }
                    ]
                    }
                }
                }
            },
            {
                "name": "streaming_agent_run_with_events",
                "description": "Streams responses asynchronously from the ADK application.\n\n        In general, you should use `async_stream_query` instead, as it has a\n        more structured API and works with the respective ADK services that\n        you have defined for the AdkApp. This method is primarily meant for\n        invocation from AgentSpace.\n\n        Args:\n            request_json (str):\n                Required. The request to stream responses for.\n        ",
                "api_mode": "async_stream",
                "parameters": {
                "required": [
                    "request_json"
                ],
                "type": "object",
                "properties": {
                    "request_json": {
                    "type": "string"
                    }
                }
                }
            }
            ],
            "deploymentSpec": {
            "env": [
                {
                "name": "GOOGLE_CLOUD_LOCATION",
                "value": "us-central1"
                },
                {
                "name": "GOOGLE_GENAI_USE_VERTEXAI",
                "value": "True"
                },
                {
                "name": "MODEL",
                "value": "gemini-3.8-flash"
                },
                {
                "name": "MODEL_LOCATION",
                "value": "global"
                },
                {
                "name": "GITLAB_URL",
                "value": "https://gitlab.com"
                },
                {
                "name": "GITLAB_PROJECT",
                "value": "movistar.com.ar/gob_ia/gobierno-core/desarrollos-propios/tito-files"
                },
                {
                "name": "GITLAB_TARGET_BRANCH",
                "value": "master"
                },
                {
                "name": "OKF_BUNDLE_DIR",
                "value": "knowledge"
                },
                {
                "name": "GITLAB_TOKEN_SECRET",
                "value": "projects/tma-gemini-enterprise/secrets/tito-gitlab-token/versions/latest"
                },
                {
                "name": "GITLAB_REVIEWERS",
                "value": "dazabala,AGUSTINA.RICO"
                },
                {
                "name": "KNOWLEDGE_DATA_STORE",
                "value": "projects/tma-gemini-enterprise/locations/global/collections/default_collection/dataStores/documentaci-n-tito_1788547235358_gcs_store"
                },
                {
                "name": "KNOWLEDGE_URI_PREFIX",
                "value": "gs://g-prod-gobiernoia-cs/okf/"
                }
            ]
            },
            "agentFramework": "google-adk",
            "sourceCodeSpec": {
            "inlineSource": {},
            "imageSpec": {}
            },
            "effectiveIdentity": "service-154372397551@gcp-sa-aiplatform-re.iam.gserviceaccount.com"
        },
        "createTime": "2026-09-04T18:08:41.567107Z",
        "updateTime": "2026-09-19T01:53:49.828443Z",
        "description": "Convierte documentos a OKF y propone la informacion nueva como merge request en tito-files.",
        "contextSpec": {
            "memoryBankConfig": {
            "generationConfig": {}
            }
        }
        },
        {
        "name": "projects/154372397551/locations/us-central1/reasoningEngines/2645141852184903680",
        "displayName": "mundial-2026-agent-runtime",
        "spec": {
            "deploymentSpec": {
            "env": [
                {
                "name": "GOOGLE_GENAI_USE_VERTEXAI",
                "value": "true"
                },
                {
                "name": "GOOGLE_CLOUD_LOCATION",
                "value": "global"
                },
                {
                "name": "AGENT_VERSION",
                "value": "0.1.0"
                },
                {
                "name": "GOOGLE_CLOUD_AGENT_ENGINE_ENABLE_TELEMETRY",
                "value": "true"
                },
                {
                "name": "OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT",
                "value": "true"
                }
            ],
            "minInstances": 1,
            "maxInstances": 10,
            "resourceLimits": {
                "cpu": "1",
                "memory": "4Gi"
            },
            "containerConcurrency": 8
            },
            "agentFramework": "google-adk",
            "sourceCodeSpec": {
            "inlineSource": {},
            "imageSpec": {}
            },
            "effectiveIdentity": "service-154372397551@gcp-sa-aiplatform-re.iam.gserviceaccount.com"
        },
        "createTime": "2026-07-05T18:30:23.066584Z",
        "updateTime": "2026-09-18T19:46:21.018711Z",
        "contextSpec": {
            "memoryBankConfig": {
            "generationConfig": {}
            }
        }
        },
        {
        "name": "projects/154372397551/locations/us-central1/reasoningEngines/6264170081358446592",
        "displayName": "tito-agent",
        "spec": {
            "classMethods": [
            {
                "name": "get_session",
                "parameters": {
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string"
                    }
                },
                "type": "object",
                "required": [
                    "user_id",
                    "session_id"
                ]
                },
                "description": "Deprecated. Use async_get_session instead.\n\n        Get a session for the given user.\n        ",
                "api_mode": ""
            },
            {
                "name": "list_sessions",
                "parameters": {
                "properties": {
                    "user_id": {
                    "type": "string"
                    }
                },
                "type": "object",
                "required": [
                    "user_id"
                ]
                },
                "description": "Deprecated. Use async_list_sessions instead.\n\n        List sessions for the given user.\n        ",
                "api_mode": ""
            },
            {
                "name": "create_session",
                "parameters": {
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "expire_time": {
                    "type": "string",
                    "nullable": true
                    },
                    "ttl": {
                    "type": "string",
                    "nullable": true
                    },
                    "session_id": {
                    "type": "string",
                    "nullable": true
                    },
                    "state": {
                    "type": "object",
                    "nullable": true
                    }
                },
                "type": "object",
                "required": [
                    "user_id"
                ]
                },
                "description": "Deprecated. Use async_create_session instead.\n\n        Creates a new session.\n        ",
                "api_mode": ""
            },
            {
                "name": "delete_session",
                "parameters": {
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string"
                    }
                },
                "type": "object",
                "required": [
                    "user_id",
                    "session_id"
                ]
                },
                "description": "Deprecated. Use async_delete_session instead.\n\n        Deletes a session for the given user.\n        ",
                "api_mode": ""
            },
            {
                "name": "async_get_session",
                "parameters": {
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string"
                    }
                },
                "type": "object",
                "required": [
                    "user_id",
                    "session_id"
                ]
                },
                "description": "Get a session for the given user.\n\n        Args:\n            user_id (str):\n                Required. The ID of the user.\n            session_id (str):\n                Required. The ID of the session.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                session service.\n\n        Returns:\n            Session: The session instance (if any). It returns None if the\n            session is not found.\n\n        Raises:\n            RuntimeError: If the session is not found.\n        ",
                "api_mode": "async"
            },
            {
                "name": "async_list_sessions",
                "parameters": {
                "properties": {
                    "user_id": {
                    "type": "string"
                    }
                },
                "type": "object",
                "required": [
                    "user_id"
                ]
                },
                "description": "List sessions for the given user.\n\n        Args:\n            user_id (str):\n                Required. The ID of the user.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                session service.\n\n        Returns:\n            ListSessionsResponse: The list of sessions.\n        ",
                "api_mode": "async"
            },
            {
                "name": "async_create_session",
                "parameters": {
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "expire_time": {
                    "type": "string",
                    "nullable": true
                    },
                    "ttl": {
                    "type": "string",
                    "nullable": true
                    },
                    "session_id": {
                    "type": "string",
                    "nullable": true
                    },
                    "state": {
                    "type": "object",
                    "nullable": true
                    }
                },
                "type": "object",
                "required": [
                    "user_id"
                ]
                },
                "description": "Creates a new session.\n\n        Args:\n            user_id (str):\n                Required. The ID of the user.\n            session_id (str):\n                Optional. The ID of the session. If not provided, an ID\n                will be generated for the session.\n            state (dict[str, Any]):\n                Optional. The initial state of the session.\n            ttl (str):\n                Optional. The time-to-live for the session.\n            expire_time (str):\n                Optional. The expiration time for the session.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                session service.\n\n        Returns:\n            Session: The newly created session instance.\n        ",
                "api_mode": "async"
            },
            {
                "name": "async_delete_session",
                "parameters": {
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string"
                    }
                },
                "type": "object",
                "required": [
                    "user_id",
                    "session_id"
                ]
                },
                "description": "Deletes a session for the given user.\n\n        Args:\n            user_id (str):\n                Required. The ID of the user.\n            session_id (str):\n                Required. The ID of the session.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                session service.\n        ",
                "api_mode": "async"
            },
            {
                "name": "async_add_session_to_memory",
                "parameters": {
                "properties": {
                    "session": {
                    "type": "object",
                    "additionalProperties": true
                    }
                },
                "type": "object",
                "required": [
                    "session"
                ]
                },
                "description": "Generates memories.\n\n        Args:\n            session (Dict[str, Any]):\n                Required. The session to use for generating memories. It should\n                be a dictionary representing an ADK Session object, e.g.\n                session.model_dump(mode=\"json\").\n        ",
                "api_mode": "async"
            },
            {
                "name": "async_search_memory",
                "parameters": {
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "query": {
                    "type": "string"
                    }
                },
                "type": "object",
                "required": [
                    "user_id",
                    "query"
                ]
                },
                "description": "Searches memories for the given user.\n\n        Args:\n            user_id: The id of the user.\n            query: The query to match the memories on.\n\n        Returns:\n            A SearchMemoryResponse containing the matching memories.\n        ",
                "api_mode": "async"
            },
            {
                "name": "stream_query",
                "parameters": {
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "run_config": {
                    "type": "object",
                    "nullable": true
                    },
                    "session_id": {
                    "type": "string",
                    "nullable": true
                    },
                    "message": {
                    "anyOf": [
                        {
                        "type": "string"
                        },
                        {
                        "type": "object",
                        "additionalProperties": true
                        }
                    ]
                    }
                },
                "type": "object",
                "required": [
                    "message",
                    "user_id"
                ]
                },
                "description": "Deprecated. Use async_stream_query instead.\n\n        Streams responses from the ADK application in response to a message.\n\n        Args:\n            message (Union[str, Dict[str, Any]]):\n                Required. The message to stream responses for.\n            user_id (str):\n                Required. The ID of the user.\n            session_id (str):\n                Optional. The ID of the session. If not provided, a new\n                session will be created for the user.\n            run_config (Optional[Dict[str, Any]]):\n                Optional. The run config to use for the query. If you want to\n                pass in a `run_config` pydantic object, you can pass in a dict\n                representing it as `run_config.model_dump(mode=\"json\")`.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                runner.\n\n        Yields:\n            The output of querying the ADK application.\n        ",
                "api_mode": "stream"
            },
            {
                "name": "async_stream_query",
                "parameters": {
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "run_config": {
                    "type": "object",
                    "nullable": true
                    },
                    "session_id": {
                    "type": "string",
                    "nullable": true
                    },
                    "message": {
                    "anyOf": [
                        {
                        "type": "string"
                        },
                        {
                        "type": "object",
                        "additionalProperties": true
                        }
                    ]
                    }
                },
                "type": "object",
                "required": [
                    "message",
                    "user_id"
                ]
                },
                "description": "Streams responses asynchronously from the ADK application.\n\n        Args:\n            message (str):\n                Required. The message to stream responses for.\n            user_id (str):\n                Required. The ID of the user.\n            session_id (str):\n                Optional. The ID of the session. If not provided, a new\n                session will be created for the user.\n            run_config (Optional[Dict[str, Any]]):\n                Optional. The run config to use for the query. If you want to\n                pass in a `run_config` pydantic object, you can pass in a dict\n                representing it as `run_config.model_dump(mode=\"json\")`.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                runner.\n\n        Yields:\n            Event dictionaries asynchronously.\n        ",
                "api_mode": "async_stream"
            },
            {
                "name": "streaming_agent_run_with_events",
                "parameters": {
                "properties": {
                    "request_json": {
                    "type": "string"
                    }
                },
                "type": "object",
                "required": [
                    "request_json"
                ]
                },
                "description": "Streams responses asynchronously from the ADK application.\n\n        In general, you should use `async_stream_query` instead, as it has a\n        more structured API and works with the respective ADK services that\n        you have defined for the AdkApp. This method is primarily meant for\n        invocation from AgentSpace.\n\n        Args:\n            request_json (str):\n                Required. The request to stream responses for.\n        ",
                "api_mode": "async_stream"
            }
            ],
            "deploymentSpec": {
            "env": [
                {
                "name": "GOOGLE_GENAI_USE_VERTEXAI",
                "value": "TRUE"
                },
                {
                "name": "GOOGLE_CLOUD_LOCATION",
                "value": "us-central1"
                },
                {
                "name": "KNOWLEDGE_BASE_DATA_STORE_ID",
                "value": "projects/154372397551/locations/global/collections/default_collection/dataStores/documentaci-n-tito_1788547235358_gcs_store"
                },
                {
                "name": "SHOW_DOCUMENT_SOURCES",
                "value": "false"
                },
                {
                "name": "AGENT_MODEL_LOCATION",
                "value": "global"
                },
                {
                "name": "JIRA_INCIDENTS_ENABLED",
                "value": "true"
                },
                {
                "name": "JIRA_ACCOUNT_EMAIL",
                "value": "jira.automate@tmoviles.com.ar"
                },
                {
                "name": "JIRA_TOKEN_SECRET",
                "value": "projects/154372397551/secrets/tito-jira-token/versions/latest"
                },
                {
                "name": "JIRA_PROJECT_KEY",
                "value": "AGSIA"
                },
                {
                "name": "JIRA_ISSUE_TYPE",
                "value": "Incidente"
                },
                {
                "name": "JIRA_AFFECTED_USER_FIELD",
                "value": "customfield_10535"
                }
            ]
            },
            "agentFramework": "google-adk",
            "sourceCodeSpec": {
            "inlineSource": {},
            "imageSpec": {}
            },
            "effectiveIdentity": "service-154372397551@gcp-sa-aiplatform-re.iam.gserviceaccount.com"
        },
        "createTime": "2026-09-10T19:51:39.075564Z",
        "updateTime": "2026-09-18T19:30:11.083032Z",
        "contextSpec": {
            "memoryBankConfig": {
            "generationConfig": {}
            }
        }
        },
        {
        "name": "projects/154372397551/locations/us-central1/reasoningEngines/5749388632838373376",
        "displayName": "agente_redactor_mail",
        "spec": {
            "packageSpec": {
            "pickleObjectGcsUri": "gs://tma-gemini-enterprise-agent-staging/agent_engine/agent_engine.pkl",
            "dependencyFilesGcsUri": "gs://tma-gemini-enterprise-agent-staging/agent_engine/dependencies.tar.gz",
            "requirementsGcsUri": "gs://tma-gemini-enterprise-agent-staging/agent_engine/requirements.txt",
            "pythonVersion": "3.13"
            },
            "classMethods": [
            {
                "description": "Deprecated. Use async_get_session instead.\n\nGet a session for the given user.\n",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id",
                    "session_id"
                ]
                },
                "api_mode": "",
                "name": "get_session"
            },
            {
                "description": "Deprecated. Use async_list_sessions instead.\n\nList sessions for the given user.\n",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id"
                ]
                },
                "api_mode": "",
                "name": "list_sessions"
            },
            {
                "description": "Deprecated. Use async_create_session instead.\n\nCreates a new session.\n",
                "parameters": {
                "type": "object",
                "properties": {
                    "state": {
                    "type": "object",
                    "nullable": true
                    },
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string",
                    "nullable": true
                    }
                },
                "required": [
                    "user_id"
                ]
                },
                "api_mode": "",
                "name": "create_session"
            },
            {
                "description": "Deprecated. Use async_delete_session instead.\n\nDeletes a session for the given user.\n",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id",
                    "session_id"
                ]
                },
                "api_mode": "",
                "name": "delete_session"
            },
            {
                "description": "Get a session for the given user.\n\nArgs:\n    user_id (str):\n        Required. The ID of the user.\n    session_id (str):\n        Required. The ID of the session.\n    **kwargs (dict[str, Any]):\n        Optional. Additional keyword arguments to pass to the\n        session service.\n\nReturns:\n    Session: The session instance (if any). It returns None if the\n    session is not found.\n\nRaises:\n    RuntimeError: If the session is not found.\n",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id",
                    "session_id"
                ]
                },
                "api_mode": "async",
                "name": "async_get_session"
            },
            {
                "description": "List sessions for the given user.\n\nArgs:\n    user_id (str):\n        Required. The ID of the user.\n    **kwargs (dict[str, Any]):\n        Optional. Additional keyword arguments to pass to the\n        session service.\n\nReturns:\n    ListSessionsResponse: The list of sessions.\n",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id"
                ]
                },
                "api_mode": "async",
                "name": "async_list_sessions"
            },
            {
                "description": "Creates a new session.\n\nArgs:\n    user_id (str):\n        Required. The ID of the user.\n    session_id (str):\n        Optional. The ID of the session. If not provided, an ID\n        will be be generated for the session.\n    state (dict[str, Any]):\n        Optional. The initial state of the session.\n    ttl (str):\n        Optional. The time-to-live for the session.\n    expire_time (str):\n        Optional. The expiration time for the session.\n    **kwargs (dict[str, Any]):\n        Optional. Additional keyword arguments to pass to the\n        session service.\n\nReturns:\n    Session: The newly created session instance.\n",
                "parameters": {
                "type": "object",
                "properties": {
                    "state": {
                    "type": "object",
                    "nullable": true
                    },
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string",
                    "nullable": true
                    }
                },
                "required": [
                    "user_id"
                ]
                },
                "api_mode": "async",
                "name": "async_create_session"
            },
            {
                "description": "Deletes a session for the given user.\n\nArgs:\n    user_id (str):\n        Required. The ID of the user.\n    session_id (str):\n        Required. The ID of the session.\n    **kwargs (dict[str, Any]):\n        Optional. Additional keyword arguments to pass to the\n        session service.\n",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id",
                    "session_id"
                ]
                },
                "api_mode": "async",
                "name": "async_delete_session"
            },
            {
                "description": "Generates memories.\n\nArgs:\n    session (Dict[str, Any]):\n        Required. The session to use for generating memories. It should\n        be a dictionary representing an ADK Session object, e.g.\n        session.model_dump(mode=\"json\").\n",
                "parameters": {
                "type": "object",
                "properties": {
                    "session": {
                    "additionalProperties": true,
                    "type": "object"
                    }
                },
                "required": [
                    "session"
                ]
                },
                "api_mode": "async",
                "name": "async_add_session_to_memory"
            },
            {
                "description": "Searches memories for the given user.\n\nArgs:\n    user_id: The id of the user.\n    query: The query to match the memories on.\n\nReturns:\n    A SearchMemoryResponse containing the matching memories.\n",
                "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                    "type": "string"
                    },
                    "user_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id",
                    "query"
                ]
                },
                "api_mode": "async",
                "name": "async_search_memory"
            },
            {
                "description": "Deprecated. Use async_stream_query instead.\n\nStreams responses from the ADK application in response to a message.\n\nArgs:\n    message (Union[str, Dict[str, Any]]):\n        Required. The message to stream responses for.\n    user_id (str):\n        Required. The ID of the user.\n    session_id (str):\n        Optional. The ID of the session. If not provided, a new\n        session will be created for the user.\n    run_config (Optional[Dict[str, Any]]):\n        Optional. The run config to use for the query. If you want to\n        pass in a `run_config` pydantic object, you can pass in a dict\n        representing it as `run_config.model_dump(mode=\"json\")`.\n    **kwargs (dict[str, Any]):\n        Optional. Additional keyword arguments to pass to the\n        runner.\n\nYields:\n    The output of querying the ADK application.\n",
                "parameters": {
                "type": "object",
                "properties": {
                    "message": {
                    "anyOf": [
                        {
                        "type": "string"
                        },
                        {
                        "additionalProperties": true,
                        "type": "object"
                        }
                    ]
                    },
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string",
                    "nullable": true
                    },
                    "run_config": {
                    "type": "object",
                    "nullable": true
                    }
                },
                "required": [
                    "message",
                    "user_id"
                ]
                },
                "api_mode": "stream",
                "name": "stream_query"
            },
            {
                "description": "Streams responses asynchronously from the ADK application.\n\nArgs:\n    message (str):\n        Required. The message to stream responses for.\n    user_id (str):\n        Required. The ID of the user.\n    session_id (str):\n        Optional. The ID of the session. If not provided, a new\n        session will be created for the user. If this is specified, then\n        `session_events` will be ignored.\n    session_events (Optional[List[Dict[str, Any]]]):\n        Optional. The session events to use for the query. This will be\n        used to initialize the session if `session_id` is not provided.\n    run_config (Optional[Dict[str, Any]]):\n        Optional. The run config to use for the query. If you want to\n        pass in a `run_config` pydantic object, you can pass in a dict\n        representing it as `run_config.model_dump(mode=\"json\")`.\n    **kwargs (dict[str, Any]):\n        Optional. Additional keyword arguments to pass to the\n        runner.\n\nYields:\n    Event dictionaries asynchronously.\n\nRaises:\n    TypeError: If message is not a string or a dictionary representing\n    a Content object.\n    ValueError: If both session_id and session_events are specified.\n",
                "parameters": {
                "type": "object",
                "properties": {
                    "message": {
                    "anyOf": [
                        {
                        "type": "string"
                        },
                        {
                        "additionalProperties": true,
                        "type": "object"
                        }
                    ]
                    },
                    "session_events": {
                    "type": "array",
                    "nullable": true
                    },
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string",
                    "nullable": true
                    },
                    "run_config": {
                    "type": "object",
                    "nullable": true
                    }
                },
                "required": [
                    "message",
                    "user_id"
                ]
                },
                "api_mode": "async_stream",
                "name": "async_stream_query"
            },
            {
                "description": "Streams responses asynchronously from the ADK application.\n\nIn general, you should use `async_stream_query` instead, as it has a\nmore structured API and works with the respective ADK services that\nyou have defined for the AdkApp. This method is primarily meant for\ninvocation from AgentSpace.\n\nArgs:\n    request_json (str):\n        Required. The request to stream responses for.\n",
                "parameters": {
                "type": "object",
                "properties": {
                    "request_json": {
                    "type": "string"
                    }
                },
                "required": [
                    "request_json"
                ]
                },
                "api_mode": "async_stream",
                "name": "streaming_agent_run_with_events"
            }
            ],
            "deploymentSpec": {
            "env": [
                {
                "name": "MODEL",
                "value": "gemini-3.8-flash"
                },
                {
                "name": "GOOGLE_GENAI_USE_VERTEXAI",
                "value": "true"
                },
                {
                "name": "GOOGLE_CLOUD_AGENT_ENGINE_ENABLE_TELEMETRY",
                "value": "true"
                },
                {
                "name": "OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT",
                "value": "EVENT_ONLY"
                },
                {
                "name": "OTEL_SEMCONV_STABILITY_OPT_IN",
                "value": "gen_ai_latest_experimental"
                },
                {
                "name": "LOGS_BUCKET_NAME",
                "value": "g-prod-gobiernoia-cs"
                },
                {
                "name": "GENAI_TELEMETRY_PATH",
                "value": "prod/intents"
                }
            ]
            },
            "agentFramework": "google-adk",
            "effectiveIdentity": "service-154372397551@gcp-sa-aiplatform-re.iam.gserviceaccount.com"
        },
        "createTime": "2026-07-06T18:56:18.092711Z",
        "updateTime": "2026-09-18T19:14:22.479852Z",
        "description": "Redacta el correo formal de aprobación o rechazo basado en los resultados de la validación.",
        "contextSpec": {
            "memoryBankConfig": {
            "generationConfig": {}
            }
        }
        },
        {
        "name": "projects/154372397551/locations/us-central1/reasoningEngines/5936592582095142912",
        "displayName": "jira-agent",
        "spec": {
            "classMethods": [
            {
                "name": "get_session",
                "api_mode": "",
                "description": "Deprecated. Use async_get_session instead.\n\n        Get a session for the given user.\n        ",
                "parameters": {
                "required": [
                    "user_id",
                    "session_id"
                ],
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string"
                    }
                }
                }
            },
            {
                "name": "list_sessions",
                "api_mode": "",
                "description": "Deprecated. Use async_list_sessions instead.\n\n        List sessions for the given user.\n        ",
                "parameters": {
                "required": [
                    "user_id"
                ],
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    }
                }
                }
            },
            {
                "name": "create_session",
                "api_mode": "",
                "description": "Deprecated. Use async_create_session instead.\n\n        Creates a new session.\n        ",
                "parameters": {
                "required": [
                    "user_id"
                ],
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "state": {
                    "type": "object",
                    "nullable": true
                    },
                    "session_id": {
                    "type": "string",
                    "nullable": true
                    },
                    "ttl": {
                    "type": "string",
                    "nullable": true
                    },
                    "expire_time": {
                    "type": "string",
                    "nullable": true
                    }
                }
                }
            },
            {
                "name": "delete_session",
                "api_mode": "",
                "description": "Deprecated. Use async_delete_session instead.\n\n        Deletes a session for the given user.\n        ",
                "parameters": {
                "required": [
                    "user_id",
                    "session_id"
                ],
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string"
                    }
                }
                }
            },
            {
                "name": "async_get_session",
                "api_mode": "async",
                "description": "Get a session for the given user.\n\n        Args:\n            user_id (str):\n                Required. The ID of the user.\n            session_id (str):\n                Required. The ID of the session.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                session service.\n\n        Returns:\n            Session: The session instance (if any). It returns None if the\n            session is not found.\n\n        Raises:\n            RuntimeError: If the session is not found.\n        ",
                "parameters": {
                "required": [
                    "user_id",
                    "session_id"
                ],
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string"
                    }
                }
                }
            },
            {
                "name": "async_list_sessions",
                "api_mode": "async",
                "description": "List sessions for the given user.\n\n        Args:\n            user_id (str):\n                Required. The ID of the user.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                session service.\n\n        Returns:\n            ListSessionsResponse: The list of sessions.\n        ",
                "parameters": {
                "required": [
                    "user_id"
                ],
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    }
                }
                }
            },
            {
                "name": "async_create_session",
                "api_mode": "async",
                "description": "Creates a new session.\n\n        Args:\n            user_id (str):\n                Required. The ID of the user.\n            session_id (str):\n                Optional. The ID of the session. If not provided, an ID\n                will be generated for the session.\n            state (dict[str, Any]):\n                Optional. The initial state of the session.\n            ttl (str):\n                Optional. The time-to-live for the session.\n            expire_time (str):\n                Optional. The expiration time for the session.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                session service.\n\n        Returns:\n            Session: The newly created session instance.\n        ",
                "parameters": {
                "required": [
                    "user_id"
                ],
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "state": {
                    "type": "object",
                    "nullable": true
                    },
                    "session_id": {
                    "type": "string",
                    "nullable": true
                    },
                    "ttl": {
                    "type": "string",
                    "nullable": true
                    },
                    "expire_time": {
                    "type": "string",
                    "nullable": true
                    }
                }
                }
            },
            {
                "name": "async_delete_session",
                "api_mode": "async",
                "description": "Deletes a session for the given user.\n\n        Args:\n            user_id (str):\n                Required. The ID of the user.\n            session_id (str):\n                Required. The ID of the session.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                session service.\n        ",
                "parameters": {
                "required": [
                    "user_id",
                    "session_id"
                ],
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string"
                    }
                }
                }
            },
            {
                "name": "async_add_session_to_memory",
                "api_mode": "async",
                "description": "Generates memories.\n\n        Args:\n            session (Dict[str, Any]):\n                Required. The session to use for generating memories. It should\n                be a dictionary representing an ADK Session object, e.g.\n                session.model_dump(mode=\"json\").\n        ",
                "parameters": {
                "required": [
                    "session"
                ],
                "type": "object",
                "properties": {
                    "session": {
                    "type": "object",
                    "additionalProperties": true
                    }
                }
                }
            },
            {
                "name": "async_search_memory",
                "api_mode": "async",
                "description": "Searches memories for the given user.\n\n        Args:\n            user_id: The id of the user.\n            query: The query to match the memories on.\n\n        Returns:\n            A SearchMemoryResponse containing the matching memories.\n        ",
                "parameters": {
                "required": [
                    "user_id",
                    "query"
                ],
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "query": {
                    "type": "string"
                    }
                }
                }
            },
            {
                "name": "stream_query",
                "api_mode": "stream",
                "description": "Deprecated. Use async_stream_query instead.\n\n        Streams responses from the ADK application in response to a message.\n\n        Args:\n            message (Union[str, Dict[str, Any]]):\n                Required. The message to stream responses for.\n            user_id (str):\n                Required. The ID of the user.\n            session_id (str):\n                Optional. The ID of the session. If not provided, a new\n                session will be created for the user.\n            run_config (Optional[Dict[str, Any]]):\n                Optional. The run config to use for the query. If you want to\n                pass in a `run_config` pydantic object, you can pass in a dict\n                representing it as `run_config.model_dump(mode=\"json\")`.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                runner.\n\n        Yields:\n            The output of querying the ADK application.\n        ",
                "parameters": {
                "required": [
                    "message",
                    "user_id"
                ],
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "run_config": {
                    "type": "object",
                    "nullable": true
                    },
                    "session_id": {
                    "type": "string",
                    "nullable": true
                    },
                    "message": {
                    "anyOf": [
                        {
                        "type": "string"
                        },
                        {
                        "type": "object",
                        "additionalProperties": true
                        }
                    ]
                    }
                }
                }
            },
            {
                "name": "async_stream_query",
                "api_mode": "async_stream",
                "description": "Streams responses asynchronously from the ADK application.\n\n        Args:\n            message (str):\n                Required. The message to stream responses for.\n            user_id (str):\n                Required. The ID of the user.\n            session_id (str):\n                Optional. The ID of the session. If not provided, a new\n                session will be created for the user. If this is specified, then\n                `session_events` will be ignored.\n            session_events (Optional[List[Dict[str, Any]]]):\n                Optional. The session events to use for the query. This will be\n                used to initialize the session if `session_id` is not provided.\n            run_config (Optional[Dict[str, Any]]):\n                Optional. The run config to use for the query. If you want to\n                pass in a `run_config` pydantic object, you can pass in a dict\n                representing it as `run_config.model_dump(mode=\"json\")`.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                runner.\n\n        Yields:\n            Event dictionaries asynchronously.\n\n        Raises:\n            TypeError: If message is not a string or a dictionary representing\n            a Content object.\n            ValueError: If both session_id and session_events are specified.\n        ",
                "parameters": {
                "required": [
                    "message",
                    "user_id"
                ],
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "run_config": {
                    "type": "object",
                    "nullable": true
                    },
                    "session_id": {
                    "type": "string",
                    "nullable": true
                    },
                    "message": {
                    "anyOf": [
                        {
                        "type": "string"
                        },
                        {
                        "type": "object",
                        "additionalProperties": true
                        }
                    ]
                    },
                    "session_events": {
                    "type": "array",
                    "nullable": true
                    }
                }
                }
            },
            {
                "name": "streaming_agent_run_with_events",
                "api_mode": "async_stream",
                "description": "Streams responses asynchronously from the ADK application.\n\n        In general, you should use `async_stream_query` instead, as it has a\n        more structured API and works with the respective ADK services that\n        you have defined for the AdkApp. This method is primarily meant for\n        invocation from AgentSpace.\n\n        Args:\n            request_json (str):\n                Required. The request to stream responses for.\n        ",
                "parameters": {
                "required": [
                    "request_json"
                ],
                "type": "object",
                "properties": {
                    "request_json": {
                    "type": "string"
                    }
                }
                }
            }
            ],
            "deploymentSpec": {
            "env": [
                {
                "name": "MODEL_PROVIDER",
                "value": "litellm"
                },
                {
                "name": "JIRA_MCP_URL",
                "value": "https://jira-mcp-server-154372397551.us-central1.run.app/mcp"
                },
                {
                "name": "GCP_SA_KEY_PATH",
                "value": "sa-key.json"
                },
                {
                "name": "JIRA_TOOLS_FILTER",
                "value": "findUsers, getUser, searchAndReconsileIssuesUsingJql, getIssue"
                },
                {
                "name": "USE_MEMORY_BANK",
                "value": "false"
                },
                {
                "name": "GOOGLE_CLOUD_LOCATION",
                "value": "us-central1"
                },
                {
                "name": "GOOGLE_GENAI_USE_VERTEXAI",
                "value": "TRUE"
                },
                {
                "name": "GEMINI_MODEL_NAME",
                "value": "gemini-2.5-flash"
                },
                {
                "name": "LITELLM_API_BASE",
                "value": "http://34.42.178.117/llm-jira-gemini"
                },
                {
                "name": "LITELLM_API_KEY",
                "value": "sk-1234"
                },
                {
                "name": "LITELLM_MODEL_NAME",
                "value": "gemini/model"
                },
                {
                "name": "LITELLM_TOKEN",
                "value": "e55f9e0911e945beadeeac4a5dcd79e2.DA815B72a6B845e6A13f995AEAE644C8"
                }
            ]
            },
            "agentFramework": "google-adk",
            "sourceCodeSpec": {
            "inlineSource": {},
            "imageSpec": {}
            },
            "effectiveIdentity": "service-154372397551@gcp-sa-aiplatform-re.iam.gserviceaccount.com"
        },
        "createTime": "2026-09-18T17:28:13.690117Z",
        "updateTime": "2026-09-18T17:38:06.603653Z",
        "contextSpec": {
            "memoryBankConfig": {
            "generationConfig": {}
            }
        }
        },
        {
        "name": "projects/154372397551/locations/us-central1/reasoningEngines/6578918478948859904",
        "spec": {
            "effectiveIdentity": "service-154372397551@gcp-sa-aiplatform-re.iam.gserviceaccount.com"
        },
        "createTime": "2026-09-18T16:53:03.278238Z",
        "updateTime": "2026-09-18T16:53:05.724292Z",
        "contextSpec": {
            "memoryBankConfig": {
            "generationConfig": {}
            }
        }
        },
        {
        "name": "projects/154372397551/locations/us-central1/reasoningEngines/5574522303556878336",
        "displayName": "agente_fastgate",
        "spec": {
            "packageSpec": {
            "pickleObjectGcsUri": "gs://tma-gemini-enterprise-agent-staging/agent_engine/agent_engine.pkl",
            "dependencyFilesGcsUri": "gs://tma-gemini-enterprise-agent-staging/agent_engine/dependencies.tar.gz",
            "requirementsGcsUri": "gs://tma-gemini-enterprise-agent-staging/agent_engine/requirements.txt",
            "pythonVersion": "3.13"
            },
            "classMethods": [
            {
                "description": "Deprecated. Use async_get_session instead.\n\n        Get a session for the given user.\n        ",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id",
                    "session_id"
                ]
                },
                "api_mode": "",
                "name": "get_session"
            },
            {
                "description": "Deprecated. Use async_list_sessions instead.\n\n        List sessions for the given user.\n        ",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id"
                ]
                },
                "api_mode": "",
                "name": "list_sessions"
            },
            {
                "description": "Deprecated. Use async_create_session instead.\n\n        Creates a new session.\n        ",
                "parameters": {
                "type": "object",
                "properties": {
                    "state": {
                    "type": "object",
                    "nullable": true
                    },
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string",
                    "nullable": true
                    }
                },
                "required": [
                    "user_id"
                ]
                },
                "api_mode": "",
                "name": "create_session"
            },
            {
                "description": "Deprecated. Use async_delete_session instead.\n\n        Deletes a session for the given user.\n        ",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id",
                    "session_id"
                ]
                },
                "api_mode": "",
                "name": "delete_session"
            },
            {
                "description": "Get a session for the given user.\n\n        Args:\n            user_id (str):\n                Required. The ID of the user.\n            session_id (str):\n                Required. The ID of the session.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                session service.\n\n        Returns:\n            Session: The session instance (if any). It returns None if the\n            session is not found.\n\n        Raises:\n            RuntimeError: If the session is not found.\n        ",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id",
                    "session_id"
                ]
                },
                "api_mode": "async",
                "name": "async_get_session"
            },
            {
                "description": "List sessions for the given user.\n\n        Args:\n            user_id (str):\n                Required. The ID of the user.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                session service.\n\n        Returns:\n            ListSessionsResponse: The list of sessions.\n        ",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id"
                ]
                },
                "api_mode": "async",
                "name": "async_list_sessions"
            },
            {
                "description": "Creates a new session.\n\n        Args:\n            user_id (str):\n                Required. The ID of the user.\n            session_id (str):\n                Optional. The ID of the session. If not provided, an ID\n                will be be generated for the session.\n            state (dict[str, Any]):\n                Optional. The initial state of the session.\n            ttl (str):\n                Optional. The time-to-live for the session.\n            expire_time (str):\n                Optional. The expiration time for the session.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                session service.\n\n        Returns:\n            Session: The newly created session instance.\n        ",
                "parameters": {
                "type": "object",
                "properties": {
                    "state": {
                    "type": "object",
                    "nullable": true
                    },
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string",
                    "nullable": true
                    }
                },
                "required": [
                    "user_id"
                ]
                },
                "api_mode": "async",
                "name": "async_create_session"
            },
            {
                "description": "Deletes a session for the given user.\n\n        Args:\n            user_id (str):\n                Required. The ID of the user.\n            session_id (str):\n                Required. The ID of the session.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                session service.\n        ",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id",
                    "session_id"
                ]
                },
                "api_mode": "async",
                "name": "async_delete_session"
            },
            {
                "description": "Generates memories.\n\n        Args:\n            session (Dict[str, Any]):\n                Required. The session to use for generating memories. It should\n                be a dictionary representing an ADK Session object, e.g.\n                session.model_dump(mode=\"json\").\n        ",
                "parameters": {
                "type": "object",
                "properties": {
                    "session": {
                    "additionalProperties": true,
                    "type": "object"
                    }
                },
                "required": [
                    "session"
                ]
                },
                "api_mode": "async",
                "name": "async_add_session_to_memory"
            },
            {
                "description": "Searches memories for the given user.\n\n        Args:\n            user_id: The id of the user.\n            query: The query to match the memories on.\n\n        Returns:\n            A SearchMemoryResponse containing the matching memories.\n        ",
                "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                    "type": "string"
                    },
                    "user_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id",
                    "query"
                ]
                },
                "api_mode": "async",
                "name": "async_search_memory"
            },
            {
                "description": "Deprecated. Use async_stream_query instead.\n\n        Streams responses from the ADK application in response to a message.\n\n        Args:\n            message (Union[str, Dict[str, Any]]):\n                Required. The message to stream responses for.\n            user_id (str):\n                Required. The ID of the user.\n            session_id (str):\n                Optional. The ID of the session. If not provided, a new\n                session will be created for the user.\n            run_config (Optional[Dict[str, Any]]):\n                Optional. The run config to use for the query. If you want to\n                pass in a `run_config` pydantic object, you can pass in a dict\n                representing it as `run_config.model_dump(mode=\"json\")`.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                runner.\n\n        Yields:\n            The output of querying the ADK application.\n        ",
                "parameters": {
                "type": "object",
                "properties": {
                    "message": {
                    "anyOf": [
                        {
                        "type": "string"
                        },
                        {
                        "additionalProperties": true,
                        "type": "object"
                        }
                    ]
                    },
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string",
                    "nullable": true
                    },
                    "run_config": {
                    "type": "object",
                    "nullable": true
                    }
                },
                "required": [
                    "message",
                    "user_id"
                ]
                },
                "api_mode": "stream",
                "name": "stream_query"
            },
            {
                "description": "Streams responses asynchronously from the ADK application.\n\n        Args:\n            message (str):\n                Required. The message to stream responses for.\n            user_id (str):\n                Required. The ID of the user.\n            session_id (str):\n                Optional. The ID of the session. If not provided, a new\n                session will be created for the user. If this is specified, then\n                `session_events` will be ignored.\n            session_events (Optional[List[Dict[str, Any]]]):\n                Optional. The session events to use for the query. This will be\n                used to initialize the session if `session_id` is not provided.\n            run_config (Optional[Dict[str, Any]]):\n                Optional. The run config to use for the query. If you want to\n                pass in a `run_config` pydantic object, you can pass in a dict\n                representing it as `run_config.model_dump(mode=\"json\")`.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                runner.\n\n        Yields:\n            Event dictionaries asynchronously.\n\n        Raises:\n            TypeError: If message is not a string or a dictionary representing\n            a Content object.\n            ValueError: If both session_id and session_events are specified.\n        ",
                "parameters": {
                "type": "object",
                "properties": {
                    "message": {
                    "anyOf": [
                        {
                        "type": "string"
                        },
                        {
                        "additionalProperties": true,
                        "type": "object"
                        }
                    ]
                    },
                    "session_events": {
                    "type": "array",
                    "nullable": true
                    },
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string",
                    "nullable": true
                    },
                    "run_config": {
                    "type": "object",
                    "nullable": true
                    }
                },
                "required": [
                    "message",
                    "user_id"
                ]
                },
                "api_mode": "async_stream",
                "name": "async_stream_query"
            },
            {
                "description": "Streams responses asynchronously from the ADK application.\n\n        In general, you should use `async_stream_query` instead, as it has a\n        more structured API and works with the respective ADK services that\n        you have defined for the AdkApp. This method is primarily meant for\n        invocation from AgentSpace.\n\n        Args:\n            request_json (str):\n                Required. The request to stream responses for.\n        ",
                "parameters": {
                "type": "object",
                "properties": {
                    "request_json": {
                    "type": "string"
                    }
                },
                "required": [
                    "request_json"
                ]
                },
                "api_mode": "async_stream",
                "name": "streaming_agent_run_with_events"
            }
            ],
            "deploymentSpec": {
            "env": [
                {
                "name": "MODEL",
                "value": "gemini-3.8-flash"
                },
                {
                "name": "GOOGLE_GENAI_USE_VERTEXAI",
                "value": "true"
                },
                {
                "name": "GOOGLE_CLOUD_AGENT_ENGINE_ENABLE_TELEMETRY",
                "value": "true"
                },
                {
                "name": "OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT",
                "value": "EVENT_ONLY"
                },
                {
                "name": "OTEL_SEMCONV_STABILITY_OPT_IN",
                "value": "gen_ai_latest_experimental"
                },
                {
                "name": "LOGS_BUCKET_NAME",
                "value": "g-prod-gobiernoia-cs"
                },
                {
                "name": "GENAI_TELEMETRY_PATH",
                "value": "prod/intents"
                }
            ]
            },
            "agentFramework": "google-adk",
            "effectiveIdentity": "service-154372397551@gcp-sa-aiplatform-re.iam.gserviceaccount.com"
        },
        "createTime": "2026-07-03T14:19:09.391972Z",
        "updateTime": "2026-09-18T16:26:39.721582Z",
        "description": "Este agente recibe un id de intent y clasifica su riesgo.",
        "contextSpec": {
            "memoryBankConfig": {
            "generationConfig": {}
            }
        }
        },
        {
        "name": "projects/154372397551/locations/us-central1/reasoningEngines/1584755246171684864",
        "displayName": "agente_validador_factibilidad",
        "spec": {
            "packageSpec": {
            "pickleObjectGcsUri": "gs://tma-gemini-enterprise-agent-staging/agent_engine/agent_engine.pkl",
            "dependencyFilesGcsUri": "gs://tma-gemini-enterprise-agent-staging/agent_engine/dependencies.tar.gz",
            "requirementsGcsUri": "gs://tma-gemini-enterprise-agent-staging/agent_engine/requirements.txt",
            "pythonVersion": "3.11"
            },
            "classMethods": [
            {
                "description": "Deprecated. Use async_get_session instead.\n\nGet a session for the given user.\n",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id",
                    "session_id"
                ]
                },
                "api_mode": "",
                "name": "get_session"
            },
            {
                "description": "Deprecated. Use async_list_sessions instead.\n\nList sessions for the given user.\n",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id"
                ]
                },
                "api_mode": "",
                "name": "list_sessions"
            },
            {
                "description": "Deprecated. Use async_create_session instead.\n\nCreates a new session.\n",
                "parameters": {
                "type": "object",
                "properties": {
                    "state": {
                    "type": "object",
                    "nullable": true
                    },
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string",
                    "nullable": true
                    }
                },
                "required": [
                    "user_id"
                ]
                },
                "api_mode": "",
                "name": "create_session"
            },
            {
                "description": "Deprecated. Use async_delete_session instead.\n\nDeletes a session for the given user.\n",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id",
                    "session_id"
                ]
                },
                "api_mode": "",
                "name": "delete_session"
            },
            {
                "description": "Get a session for the given user.\n\nArgs:\n    user_id (str):\n        Required. The ID of the user.\n    session_id (str):\n        Required. The ID of the session.\n    **kwargs (dict[str, Any]):\n        Optional. Additional keyword arguments to pass to the\n        session service.\n\nReturns:\n    Session: The session instance (if any). It returns None if the\n    session is not found.\n\nRaises:\n    RuntimeError: If the session is not found.\n",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id",
                    "session_id"
                ]
                },
                "api_mode": "async",
                "name": "async_get_session"
            },
            {
                "description": "List sessions for the given user.\n\nArgs:\n    user_id (str):\n        Required. The ID of the user.\n    **kwargs (dict[str, Any]):\n        Optional. Additional keyword arguments to pass to the\n        session service.\n\nReturns:\n    ListSessionsResponse: The list of sessions.\n",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id"
                ]
                },
                "api_mode": "async",
                "name": "async_list_sessions"
            },
            {
                "description": "Creates a new session.\n\nArgs:\n    user_id (str):\n        Required. The ID of the user.\n    session_id (str):\n        Optional. The ID of the session. If not provided, an ID\n        will be be generated for the session.\n    state (dict[str, Any]):\n        Optional. The initial state of the session.\n    ttl (str):\n        Optional. The time-to-live for the session.\n    expire_time (str):\n        Optional. The expiration time for the session.\n    **kwargs (dict[str, Any]):\n        Optional. Additional keyword arguments to pass to the\n        session service.\n\nReturns:\n    Session: The newly created session instance.\n",
                "parameters": {
                "type": "object",
                "properties": {
                    "state": {
                    "type": "object",
                    "nullable": true
                    },
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string",
                    "nullable": true
                    }
                },
                "required": [
                    "user_id"
                ]
                },
                "api_mode": "async",
                "name": "async_create_session"
            },
            {
                "description": "Deletes a session for the given user.\n\nArgs:\n    user_id (str):\n        Required. The ID of the user.\n    session_id (str):\n        Required. The ID of the session.\n    **kwargs (dict[str, Any]):\n        Optional. Additional keyword arguments to pass to the\n        session service.\n",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id",
                    "session_id"
                ]
                },
                "api_mode": "async",
                "name": "async_delete_session"
            },
            {
                "description": "Generates memories.\n\nArgs:\n    session (Dict[str, Any]):\n        Required. The session to use for generating memories. It should\n        be a dictionary representing an ADK Session object, e.g.\n        session.model_dump(mode=\"json\").\n",
                "parameters": {
                "type": "object",
                "properties": {
                    "session": {
                    "additionalProperties": true,
                    "type": "object"
                    }
                },
                "required": [
                    "session"
                ]
                },
                "api_mode": "async",
                "name": "async_add_session_to_memory"
            },
            {
                "description": "Searches memories for the given user.\n\nArgs:\n    user_id: The id of the user.\n    query: The query to match the memories on.\n\nReturns:\n    A SearchMemoryResponse containing the matching memories.\n",
                "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                    "type": "string"
                    },
                    "user_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id",
                    "query"
                ]
                },
                "api_mode": "async",
                "name": "async_search_memory"
            },
            {
                "description": "Deprecated. Use async_stream_query instead.\n\nStreams responses from the ADK application in response to a message.\n\nArgs:\n    message (Union[str, Dict[str, Any]]):\n        Required. The message to stream responses for.\n    user_id (str):\n        Required. The ID of the user.\n    session_id (str):\n        Optional. The ID of the session. If not provided, a new\n        session will be created for the user.\n    run_config (Optional[Dict[str, Any]]):\n        Optional. The run config to use for the query. If you want to\n        pass in a `run_config` pydantic object, you can pass in a dict\n        representing it as `run_config.model_dump(mode=\"json\")`.\n    **kwargs (dict[str, Any]):\n        Optional. Additional keyword arguments to pass to the\n        runner.\n\nYields:\n    The output of querying the ADK application.\n",
                "parameters": {
                "type": "object",
                "properties": {
                    "message": {
                    "anyOf": [
                        {
                        "type": "string"
                        },
                        {
                        "additionalProperties": true,
                        "type": "object"
                        }
                    ]
                    },
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string",
                    "nullable": true
                    },
                    "run_config": {
                    "type": "object",
                    "nullable": true
                    }
                },
                "required": [
                    "message",
                    "user_id"
                ]
                },
                "api_mode": "stream",
                "name": "stream_query"
            },
            {
                "description": "Streams responses asynchronously from the ADK application.\n\nArgs:\n    message (str):\n        Required. The message to stream responses for.\n    user_id (str):\n        Required. The ID of the user.\n    session_id (str):\n        Optional. The ID of the session. If not provided, a new\n        session will be created for the user. If this is specified, then\n        `session_events` will be ignored.\n    session_events (Optional[List[Dict[str, Any]]]):\n        Optional. The session events to use for the query. This will be\n        used to initialize the session if `session_id` is not provided.\n    run_config (Optional[Dict[str, Any]]):\n        Optional. The run config to use for the query. If you want to\n        pass in a `run_config` pydantic object, you can pass in a dict\n        representing it as `run_config.model_dump(mode=\"json\")`.\n    **kwargs (dict[str, Any]):\n        Optional. Additional keyword arguments to pass to the\n        runner.\n\nYields:\n    Event dictionaries asynchronously.\n\nRaises:\n    TypeError: If message is not a string or a dictionary representing\n    a Content object.\n    ValueError: If both session_id and session_events are specified.\n",
                "parameters": {
                "type": "object",
                "properties": {
                    "message": {
                    "anyOf": [
                        {
                        "type": "string"
                        },
                        {
                        "additionalProperties": true,
                        "type": "object"
                        }
                    ]
                    },
                    "session_events": {
                    "type": "array",
                    "nullable": true
                    },
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string",
                    "nullable": true
                    },
                    "run_config": {
                    "type": "object",
                    "nullable": true
                    }
                },
                "required": [
                    "message",
                    "user_id"
                ]
                },
                "api_mode": "async_stream",
                "name": "async_stream_query"
            },
            {
                "description": "Streams responses asynchronously from the ADK application.\n\nIn general, you should use `async_stream_query` instead, as it has a\nmore structured API and works with the respective ADK services that\nyou have defined for the AdkApp. This method is primarily meant for\ninvocation from AgentSpace.\n\nArgs:\n    request_json (str):\n        Required. The request to stream responses for.\n",
                "parameters": {
                "type": "object",
                "properties": {
                    "request_json": {
                    "type": "string"
                    }
                },
                "required": [
                    "request_json"
                ]
                },
                "api_mode": "async_stream",
                "name": "streaming_agent_run_with_events"
            }
            ],
            "deploymentSpec": {
            "env": [
                {
                "name": "MODEL",
                "value": "gemini-3.8-flash"
                },
                {
                "name": "GOOGLE_GENAI_USE_VERTEXAI",
                "value": "true"
                },
                {
                "name": "GOOGLE_CLOUD_AGENT_ENGINE_ENABLE_TELEMETRY",
                "value": "true"
                },
                {
                "name": "OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT",
                "value": "EVENT_ONLY"
                },
                {
                "name": "OTEL_SEMCONV_STABILITY_OPT_IN",
                "value": "gen_ai_latest_experimental"
                },
                {
                "name": "LOGS_BUCKET_NAME",
                "value": "g-prod-gobiernoia-cs"
                },
                {
                "name": "GENAI_TELEMETRY_PATH",
                "value": "prod/intents"
                }
            ]
            },
            "agentFramework": "google-adk",
            "effectiveIdentity": "service-154372397551@gcp-sa-aiplatform-re.iam.gserviceaccount.com"
        },
        "createTime": "2026-07-02T14:44:45.705893Z",
        "updateTime": "2026-09-18T16:07:07.120762Z",
        "description": "Evalúa si una iniciativa de IA puede implementarse con el stack tecnológico disponible en la organización y clasifica su tipo de implementación como pro code o no code.",
        "contextSpec": {
            "memoryBankConfig": {
            "generationConfig": {}
            }
        }
        },
        {
        "name": "projects/154372397551/locations/us-central1/reasoningEngines/2537266567360544768",
        "displayName": "agente_validador_impacto",
        "spec": {
            "packageSpec": {
            "pickleObjectGcsUri": "gs://tma-gemini-enterprise-agent-staging/agent_engine/agent_engine.pkl",
            "dependencyFilesGcsUri": "gs://tma-gemini-enterprise-agent-staging/agent_engine/dependencies.tar.gz",
            "requirementsGcsUri": "gs://tma-gemini-enterprise-agent-staging/agent_engine/requirements.txt",
            "pythonVersion": "3.11"
            },
            "classMethods": [
            {
                "description": "Deprecated. Use async_get_session instead.\n\n        Get a session for the given user.\n        ",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id",
                    "session_id"
                ]
                },
                "api_mode": "",
                "name": "get_session"
            },
            {
                "description": "Deprecated. Use async_list_sessions instead.\n\n        List sessions for the given user.\n        ",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id"
                ]
                },
                "api_mode": "",
                "name": "list_sessions"
            },
            {
                "description": "Deprecated. Use async_create_session instead.\n\n        Creates a new session.\n        ",
                "parameters": {
                "type": "object",
                "properties": {
                    "state": {
                    "type": "object",
                    "nullable": true
                    },
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string",
                    "nullable": true
                    }
                },
                "required": [
                    "user_id"
                ]
                },
                "api_mode": "",
                "name": "create_session"
            },
            {
                "description": "Deprecated. Use async_delete_session instead.\n\n        Deletes a session for the given user.\n        ",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id",
                    "session_id"
                ]
                },
                "api_mode": "",
                "name": "delete_session"
            },
            {
                "description": "Get a session for the given user.\n\n        Args:\n            user_id (str):\n                Required. The ID of the user.\n            session_id (str):\n                Required. The ID of the session.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                session service.\n\n        Returns:\n            Session: The session instance (if any). It returns None if the\n            session is not found.\n\n        Raises:\n            RuntimeError: If the session is not found.\n        ",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id",
                    "session_id"
                ]
                },
                "api_mode": "async",
                "name": "async_get_session"
            },
            {
                "description": "List sessions for the given user.\n\n        Args:\n            user_id (str):\n                Required. The ID of the user.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                session service.\n\n        Returns:\n            ListSessionsResponse: The list of sessions.\n        ",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id"
                ]
                },
                "api_mode": "async",
                "name": "async_list_sessions"
            },
            {
                "description": "Creates a new session.\n\n        Args:\n            user_id (str):\n                Required. The ID of the user.\n            session_id (str):\n                Optional. The ID of the session. If not provided, an ID\n                will be be generated for the session.\n            state (dict[str, Any]):\n                Optional. The initial state of the session.\n            ttl (str):\n                Optional. The time-to-live for the session.\n            expire_time (str):\n                Optional. The expiration time for the session.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                session service.\n\n        Returns:\n            Session: The newly created session instance.\n        ",
                "parameters": {
                "type": "object",
                "properties": {
                    "state": {
                    "type": "object",
                    "nullable": true
                    },
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string",
                    "nullable": true
                    }
                },
                "required": [
                    "user_id"
                ]
                },
                "api_mode": "async",
                "name": "async_create_session"
            },
            {
                "description": "Deletes a session for the given user.\n\n        Args:\n            user_id (str):\n                Required. The ID of the user.\n            session_id (str):\n                Required. The ID of the session.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                session service.\n        ",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id",
                    "session_id"
                ]
                },
                "api_mode": "async",
                "name": "async_delete_session"
            },
            {
                "description": "Generates memories.\n\n        Args:\n            session (Dict[str, Any]):\n                Required. The session to use for generating memories. It should\n                be a dictionary representing an ADK Session object, e.g.\n                session.model_dump(mode=\"json\").\n        ",
                "parameters": {
                "type": "object",
                "properties": {
                    "session": {
                    "additionalProperties": true,
                    "type": "object"
                    }
                },
                "required": [
                    "session"
                ]
                },
                "api_mode": "async",
                "name": "async_add_session_to_memory"
            },
            {
                "description": "Searches memories for the given user.\n\n        Args:\n            user_id: The id of the user.\n            query: The query to match the memories on.\n\n        Returns:\n            A SearchMemoryResponse containing the matching memories.\n        ",
                "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                    "type": "string"
                    },
                    "user_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id",
                    "query"
                ]
                },
                "api_mode": "async",
                "name": "async_search_memory"
            },
            {
                "description": "Deprecated. Use async_stream_query instead.\n\n        Streams responses from the ADK application in response to a message.\n\n        Args:\n            message (Union[str, Dict[str, Any]]):\n                Required. The message to stream responses for.\n            user_id (str):\n                Required. The ID of the user.\n            session_id (str):\n                Optional. The ID of the session. If not provided, a new\n                session will be created for the user.\n            run_config (Optional[Dict[str, Any]]):\n                Optional. The run config to use for the query. If you want to\n                pass in a `run_config` pydantic object, you can pass in a dict\n                representing it as `run_config.model_dump(mode=\"json\")`.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                runner.\n\n        Yields:\n            The output of querying the ADK application.\n        ",
                "parameters": {
                "type": "object",
                "properties": {
                    "message": {
                    "anyOf": [
                        {
                        "type": "string"
                        },
                        {
                        "additionalProperties": true,
                        "type": "object"
                        }
                    ]
                    },
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string",
                    "nullable": true
                    },
                    "run_config": {
                    "type": "object",
                    "nullable": true
                    }
                },
                "required": [
                    "message",
                    "user_id"
                ]
                },
                "api_mode": "stream",
                "name": "stream_query"
            },
            {
                "description": "Streams responses asynchronously from the ADK application.\n\n        Args:\n            message (str):\n                Required. The message to stream responses for.\n            user_id (str):\n                Required. The ID of the user.\n            session_id (str):\n                Optional. The ID of the session. If not provided, a new\n                session will be created for the user. If this is specified, then\n                `session_events` will be ignored.\n            session_events (Optional[List[Dict[str, Any]]]):\n                Optional. The session events to use for the query. This will be\n                used to initialize the session if `session_id` is not provided.\n            run_config (Optional[Dict[str, Any]]):\n                Optional. The run config to use for the query. If you want to\n                pass in a `run_config` pydantic object, you can pass in a dict\n                representing it as `run_config.model_dump(mode=\"json\")`.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                runner.\n\n        Yields:\n            Event dictionaries asynchronously.\n\n        Raises:\n            TypeError: If message is not a string or a dictionary representing\n            a Content object.\n            ValueError: If both session_id and session_events are specified.\n        ",
                "parameters": {
                "type": "object",
                "properties": {
                    "message": {
                    "anyOf": [
                        {
                        "type": "string"
                        },
                        {
                        "additionalProperties": true,
                        "type": "object"
                        }
                    ]
                    },
                    "session_events": {
                    "type": "array",
                    "nullable": true
                    },
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string",
                    "nullable": true
                    },
                    "run_config": {
                    "type": "object",
                    "nullable": true
                    }
                },
                "required": [
                    "message",
                    "user_id"
                ]
                },
                "api_mode": "async_stream",
                "name": "async_stream_query"
            },
            {
                "description": "Streams responses asynchronously from the ADK application.\n\n        In general, you should use `async_stream_query` instead, as it has a\n        more structured API and works with the respective ADK services that\n        you have defined for the AdkApp. This method is primarily meant for\n        invocation from AgentSpace.\n\n        Args:\n            request_json (str):\n                Required. The request to stream responses for.\n        ",
                "parameters": {
                "type": "object",
                "properties": {
                    "request_json": {
                    "type": "string"
                    }
                },
                "required": [
                    "request_json"
                ]
                },
                "api_mode": "async_stream",
                "name": "streaming_agent_run_with_events"
            }
            ],
            "deploymentSpec": {
            "env": [
                {
                "name": "MODEL",
                "value": "gemini-3.8-flash"
                },
                {
                "name": "GOOGLE_GENAI_USE_VERTEXAI",
                "value": "true"
                },
                {
                "name": "GOOGLE_CLOUD_AGENT_ENGINE_ENABLE_TELEMETRY",
                "value": "true"
                },
                {
                "name": "OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT",
                "value": "EVENT_ONLY"
                },
                {
                "name": "OTEL_SEMCONV_STABILITY_OPT_IN",
                "value": "gen_ai_latest_experimental"
                },
                {
                "name": "LOGS_BUCKET_NAME",
                "value": "g-prod-gobiernoia-cs"
                },
                {
                "name": "GENAI_TELEMETRY_PATH",
                "value": "prod/intents"
                }
            ]
            },
            "agentFramework": "google-adk",
            "effectiveIdentity": "service-154372397551@gcp-sa-aiplatform-re.iam.gserviceaccount.com"
        },
        "createTime": "2026-07-02T14:41:53.598035Z",
        "updateTime": "2026-09-18T16:00:26.676680Z",
        "description": "Agente especializado en determinar el valor de negocio y el nivel de autonomía asociado a un caso de uso de IA.",
        "contextSpec": {
            "memoryBankConfig": {
            "generationConfig": {}
            }
        }
        },
        {
        "name": "projects/154372397551/locations/us-central1/reasoningEngines/1315383693459587072",
        "displayName": "agente_validador_integridad",
        "spec": {
            "packageSpec": {
            "pickleObjectGcsUri": "gs://tma-gemini-enterprise-agent-staging/agent_engine/agent_engine.pkl",
            "dependencyFilesGcsUri": "gs://tma-gemini-enterprise-agent-staging/agent_engine/dependencies.tar.gz",
            "requirementsGcsUri": "gs://tma-gemini-enterprise-agent-staging/agent_engine/requirements.txt",
            "pythonVersion": "3.11"
            },
            "classMethods": [
            {
                "description": "Deprecated. Use async_get_session instead.\n\n        Get a session for the given user.\n        ",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id",
                    "session_id"
                ]
                },
                "api_mode": "",
                "name": "get_session"
            },
            {
                "description": "Deprecated. Use async_list_sessions instead.\n\n        List sessions for the given user.\n        ",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id"
                ]
                },
                "api_mode": "",
                "name": "list_sessions"
            },
            {
                "description": "Deprecated. Use async_create_session instead.\n\n        Creates a new session.\n        ",
                "parameters": {
                "type": "object",
                "properties": {
                    "state": {
                    "type": "object",
                    "nullable": true
                    },
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string",
                    "nullable": true
                    }
                },
                "required": [
                    "user_id"
                ]
                },
                "api_mode": "",
                "name": "create_session"
            },
            {
                "description": "Deprecated. Use async_delete_session instead.\n\n        Deletes a session for the given user.\n        ",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id",
                    "session_id"
                ]
                },
                "api_mode": "",
                "name": "delete_session"
            },
            {
                "description": "Get a session for the given user.\n\n        Args:\n            user_id (str):\n                Required. The ID of the user.\n            session_id (str):\n                Required. The ID of the session.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                session service.\n\n        Returns:\n            Session: The session instance (if any). It returns None if the\n            session is not found.\n\n        Raises:\n            RuntimeError: If the session is not found.\n        ",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id",
                    "session_id"
                ]
                },
                "api_mode": "async",
                "name": "async_get_session"
            },
            {
                "description": "List sessions for the given user.\n\n        Args:\n            user_id (str):\n                Required. The ID of the user.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                session service.\n\n        Returns:\n            ListSessionsResponse: The list of sessions.\n        ",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id"
                ]
                },
                "api_mode": "async",
                "name": "async_list_sessions"
            },
            {
                "description": "Creates a new session.\n\n        Args:\n            user_id (str):\n                Required. The ID of the user.\n            session_id (str):\n                Optional. The ID of the session. If not provided, an ID\n                will be be generated for the session.\n            state (dict[str, Any]):\n                Optional. The initial state of the session.\n            ttl (str):\n                Optional. The time-to-live for the session.\n            expire_time (str):\n                Optional. The expiration time for the session.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                session service.\n\n        Returns:\n            Session: The newly created session instance.\n        ",
                "parameters": {
                "type": "object",
                "properties": {
                    "state": {
                    "type": "object",
                    "nullable": true
                    },
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string",
                    "nullable": true
                    }
                },
                "required": [
                    "user_id"
                ]
                },
                "api_mode": "async",
                "name": "async_create_session"
            },
            {
                "description": "Deletes a session for the given user.\n\n        Args:\n            user_id (str):\n                Required. The ID of the user.\n            session_id (str):\n                Required. The ID of the session.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                session service.\n        ",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id",
                    "session_id"
                ]
                },
                "api_mode": "async",
                "name": "async_delete_session"
            },
            {
                "description": "Generates memories.\n\n        Args:\n            session (Dict[str, Any]):\n                Required. The session to use for generating memories. It should\n                be a dictionary representing an ADK Session object, e.g.\n                session.model_dump(mode=\"json\").\n        ",
                "parameters": {
                "type": "object",
                "properties": {
                    "session": {
                    "additionalProperties": true,
                    "type": "object"
                    }
                },
                "required": [
                    "session"
                ]
                },
                "api_mode": "async",
                "name": "async_add_session_to_memory"
            },
            {
                "description": "Searches memories for the given user.\n\n        Args:\n            user_id: The id of the user.\n            query: The query to match the memories on.\n\n        Returns:\n            A SearchMemoryResponse containing the matching memories.\n        ",
                "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                    "type": "string"
                    },
                    "user_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id",
                    "query"
                ]
                },
                "api_mode": "async",
                "name": "async_search_memory"
            },
            {
                "description": "Deprecated. Use async_stream_query instead.\n\n        Streams responses from the ADK application in response to a message.\n\n        Args:\n            message (Union[str, Dict[str, Any]]):\n                Required. The message to stream responses for.\n            user_id (str):\n                Required. The ID of the user.\n            session_id (str):\n                Optional. The ID of the session. If not provided, a new\n                session will be created for the user.\n            run_config (Optional[Dict[str, Any]]):\n                Optional. The run config to use for the query. If you want to\n                pass in a `run_config` pydantic object, you can pass in a dict\n                representing it as `run_config.model_dump(mode=\"json\")`.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                runner.\n\n        Yields:\n            The output of querying the ADK application.\n        ",
                "parameters": {
                "type": "object",
                "properties": {
                    "message": {
                    "anyOf": [
                        {
                        "type": "string"
                        },
                        {
                        "additionalProperties": true,
                        "type": "object"
                        }
                    ]
                    },
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string",
                    "nullable": true
                    },
                    "run_config": {
                    "type": "object",
                    "nullable": true
                    }
                },
                "required": [
                    "message",
                    "user_id"
                ]
                },
                "api_mode": "stream",
                "name": "stream_query"
            },
            {
                "description": "Streams responses asynchronously from the ADK application.\n\n        Args:\n            message (str):\n                Required. The message to stream responses for.\n            user_id (str):\n                Required. The ID of the user.\n            session_id (str):\n                Optional. The ID of the session. If not provided, a new\n                session will be created for the user. If this is specified, then\n                `session_events` will be ignored.\n            session_events (Optional[List[Dict[str, Any]]]):\n                Optional. The session events to use for the query. This will be\n                used to initialize the session if `session_id` is not provided.\n            run_config (Optional[Dict[str, Any]]):\n                Optional. The run config to use for the query. If you want to\n                pass in a `run_config` pydantic object, you can pass in a dict\n                representing it as `run_config.model_dump(mode=\"json\")`.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                runner.\n\n        Yields:\n            Event dictionaries asynchronously.\n\n        Raises:\n            TypeError: If message is not a string or a dictionary representing\n            a Content object.\n            ValueError: If both session_id and session_events are specified.\n        ",
                "parameters": {
                "type": "object",
                "properties": {
                    "message": {
                    "anyOf": [
                        {
                        "type": "string"
                        },
                        {
                        "additionalProperties": true,
                        "type": "object"
                        }
                    ]
                    },
                    "session_events": {
                    "type": "array",
                    "nullable": true
                    },
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string",
                    "nullable": true
                    },
                    "run_config": {
                    "type": "object",
                    "nullable": true
                    }
                },
                "required": [
                    "message",
                    "user_id"
                ]
                },
                "api_mode": "async_stream",
                "name": "async_stream_query"
            },
            {
                "description": "Streams responses asynchronously from the ADK application.\n\n        In general, you should use `async_stream_query` instead, as it has a\n        more structured API and works with the respective ADK services that\n        you have defined for the AdkApp. This method is primarily meant for\n        invocation from AgentSpace.\n\n        Args:\n            request_json (str):\n                Required. The request to stream responses for.\n        ",
                "parameters": {
                "type": "object",
                "properties": {
                    "request_json": {
                    "type": "string"
                    }
                },
                "required": [
                    "request_json"
                ]
                },
                "api_mode": "async_stream",
                "name": "streaming_agent_run_with_events"
            }
            ],
            "deploymentSpec": {
            "env": [
                {
                "name": "MODEL",
                "value": "gemini-3.8-flash"
                },
                {
                "name": "GOOGLE_GENAI_USE_VERTEXAI",
                "value": "true"
                },
                {
                "name": "GOOGLE_CLOUD_AGENT_ENGINE_ENABLE_TELEMETRY",
                "value": "true"
                },
                {
                "name": "OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT",
                "value": "EVENT_ONLY"
                },
                {
                "name": "OTEL_SEMCONV_STABILITY_OPT_IN",
                "value": "gen_ai_latest_experimental"
                },
                {
                "name": "LOGS_BUCKET_NAME",
                "value": "g-prod-gobiernoia-cs"
                },
                {
                "name": "GENAI_TELEMETRY_PATH",
                "value": "prod/intents"
                }
            ]
            },
            "agentFramework": "google-adk",
            "effectiveIdentity": "service-154372397551@gcp-sa-aiplatform-re.iam.gserviceaccount.com"
        },
        "createTime": "2026-07-02T14:35:22.957146Z",
        "updateTime": "2026-09-18T15:45:48.450025Z",
        "description": "Valida la integridad y completitud del JSON de iniciativa recibido.",
        "contextSpec": {
            "memoryBankConfig": {
            "generationConfig": {}
            }
        }
        },
        {
        "name": "projects/154372397551/locations/us-central1/reasoningEngines/5439789248200835072",
        "spec": {
            "effectiveIdentity": "service-154372397551@gcp-sa-aiplatform-re.iam.gserviceaccount.com"
        },
        "createTime": "2026-09-18T13:24:57.035462Z",
        "updateTime": "2026-09-18T13:24:59.540282Z",
        "contextSpec": {
            "memoryBankConfig": {
            "generationConfig": {}
            }
        }
        },
        {
        "name": "projects/154372397551/locations/us-central1/reasoningEngines/4881195559848771584",
        "spec": {
            "effectiveIdentity": "service-154372397551@gcp-sa-aiplatform-re.iam.gserviceaccount.com"
        },
        "createTime": "2026-09-17T14:07:25.095918Z",
        "updateTime": "2026-09-17T14:11:14.450861Z",
        "contextSpec": {
            "memoryBankConfig": {
            "generationConfig": {}
            }
        }
        },
        {
        "name": "projects/154372397551/locations/us-central1/reasoningEngines/6891489843516276736",
        "spec": {
            "effectiveIdentity": "service-154372397551@gcp-sa-aiplatform-re.iam.gserviceaccount.com"
        },
        "createTime": "2026-09-17T13:45:51.053442Z",
        "updateTime": "2026-09-17T13:49:38.079244Z",
        "contextSpec": {
            "memoryBankConfig": {
            "generationConfig": {}
            }
        }
        },
        {
        "name": "projects/154372397551/locations/us-central1/reasoningEngines/4457294244922523648",
        "spec": {
            "effectiveIdentity": "service-154372397551@gcp-sa-aiplatform-re.iam.gserviceaccount.com"
        },
        "createTime": "2026-09-17T13:45:19.290314Z",
        "updateTime": "2026-09-17T13:48:53.238872Z",
        "contextSpec": {
            "memoryBankConfig": {
            "generationConfig": {}
            }
        }
        },
        {
        "name": "projects/154372397551/locations/us-central1/reasoningEngines/7555770788553424896",
        "spec": {
            "effectiveIdentity": "service-154372397551@gcp-sa-aiplatform-re.iam.gserviceaccount.com"
        },
        "createTime": "2026-09-17T13:42:31.293545Z",
        "updateTime": "2026-09-17T13:47:28.301717Z",
        "contextSpec": {
            "memoryBankConfig": {
            "generationConfig": {}
            }
        }
        },
        {
        "name": "projects/154372397551/locations/us-central1/reasoningEngines/951241935014592512",
        "spec": {
            "effectiveIdentity": "service-154372397551@gcp-sa-aiplatform-re.iam.gserviceaccount.com"
        },
        "createTime": "2026-09-17T13:43:03.301882Z",
        "updateTime": "2026-09-17T13:45:28.020201Z",
        "contextSpec": {
            "memoryBankConfig": {
            "generationConfig": {}
            }
        }
        },
        {
        "name": "projects/154372397551/locations/us-central1/reasoningEngines/8886602070627450880",
        "displayName": "christmas_tree_agent_engine_custom",
        "spec": {
            "effectiveIdentity": "service-154372397551@gcp-sa-aiplatform-re.iam.gserviceaccount.com"
        },
        "createTime": "2026-09-09T16:16:14.644630Z",
        "updateTime": "2026-09-09T16:16:17.426203Z",
        "contextSpec": {
            "memoryBankConfig": {
            "generationConfig": {
                "model": "projects/tma-gemini-enterprise/locations/us-central1/publishers/google/models/gemini-3.5-flash"
            },
            "customizationConfigs": [
                {
                "memoryTopics": [
                    {
                    "customMemoryTopic": {
                        "label": "sweater_preference",
                        "description": "Extract the user's preferences for sweater styles, patterns, and designs. Include:\n                - Specific patterns (snowflake, reindeer, geometric, fair isle, solid, etc.)\n                - Style preferences (chunky knit, cardigan, pullover, turtleneck, oversized, fitted)\n                - Color preferences (red, green, navy, pastel, etc.)\n                - Material preferences if mentioned (wool, cotton, cashmere, itchy/soft)\n                - Themes (retro, modern, ugly christmas sweater, elegant)\n                \n                Example: \"User wants a retro style sweater with a pixelated reindeer pattern.\"\n                Example: \"User prefers dark blue colors and hates itchy wool.\"\n                "
                    }
                    },
                    {
                    "customMemoryTopic": {
                        "label": "personal_context",
                        "description": "Extract the user's personal context including hobbies, pets, interests, job, and preferred scenes. Include:\n                - Hobbies and activities (skiing, reading, gaming, cooking, etc.)\n                - Pets (type, breed, name, color)\n                - Job or profession if relevant to their style\n                - General interests (sci-fi, nature, vintage, tech)\n                - Preferred scenes or vibes (cozy fireplace, snowy mountain, cyberpunk city, beach)\n                \n                Example: \"User has a golden retriever named Max.\"\n                Example: \"User loves skiing and wants a snowy mountain background.\"\n                Example: \"User is a software engineer who likes cyberpunk aesthetics.\"\n                "
                    }
                    }
                ],
                "generateMemoriesExamples": [
                    {
                    "conversationSource": {
                        "events": [
                        {
                            "content": {
                            "role": "user",
                            "parts": [
                                {
                                "text": "I want a sweater that matches my dog. He's a golden retriever."
                                }
                            ]
                            }
                        },
                        {
                            "content": {
                            "role": "model",
                            "parts": [
                                {
                                "text": "That sounds adorable! A golden retriever themed sweater would be great. Do you want a picture of him on it or just matching colors?"
                                }
                            ]
                            }
                        },
                        {
                            "content": {
                            "role": "user",
                            "parts": [
                                {
                                "text": "Maybe just the color, like a golden yellow. And I like skiing, so maybe add some snowflakes."
                                }
                            ]
                            }
                        }
                        ]
                    },
                    "generatedMemories": [
                        {
                        "fact": "User has a golden retriever dog"
                        },
                        {
                        "fact": "User prefers a golden yellow color for their sweater"
                        },
                        {
                        "fact": "User likes skiing"
                        },
                        {
                        "fact": "User wants snowflake patterns on their sweater"
                        }
                    ]
                    },
                    {
                    "conversationSource": {
                        "events": [
                        {
                            "content": {
                            "role": "user",
                            "parts": [
                                {
                                "text": "I'm a programmer, so I want something geeky. Maybe a matrix style?"
                                }
                            ]
                            }
                        },
                        {
                            "content": {
                            "role": "model",
                            "parts": [
                                {
                                "text": "A Matrix style sweater sounds cool! We could do falling code rain patterns."
                                }
                            ]
                            }
                        },
                        {
                            "content": {
                            "role": "user",
                            "parts": [
                                {
                                "text": "Yes! Green code on black. And make it a hoodie style if possible."
                                }
                            ]
                            }
                        }
                        ]
                    },
                    "generatedMemories": [
                        {
                        "fact": "User is a programmer"
                        },
                        {
                        "fact": "User wants a 'Matrix' style sweater with falling code rain pattern"
                        },
                        {
                        "fact": "User prefers green code on black background"
                        },
                        {
                        "fact": "User prefers hoodie style sweaters"
                        }
                    ]
                    }
                ]
                }
            ]
            }
        }
        },
        {
        "name": "projects/154372397551/locations/us-central1/reasoningEngines/748597543968964608",
        "displayName": "christmas_tree_agent_engine_custom",
        "spec": {
            "effectiveIdentity": "service-154372397551@gcp-sa-aiplatform-re.iam.gserviceaccount.com"
        },
        "createTime": "2026-09-09T16:03:06.554755Z",
        "updateTime": "2026-09-09T16:03:09.141174Z",
        "contextSpec": {
            "memoryBankConfig": {
            "generationConfig": {
                "model": "projects/tma-gemini-enterprise/locations/us-central1/publishers/google/models/gemini-3.5-flash"
            },
            "customizationConfigs": [
                {
                "memoryTopics": [
                    {
                    "customMemoryTopic": {
                        "label": "sweater_preference",
                        "description": "Extract the user's preferences for sweater styles, patterns, and designs. Include:\n                - Specific patterns (snowflake, reindeer, geometric, fair isle, solid, etc.)\n                - Style preferences (chunky knit, cardigan, pullover, turtleneck, oversized, fitted)\n                - Color preferences (red, green, navy, pastel, etc.)\n                - Material preferences if mentioned (wool, cotton, cashmere, itchy/soft)\n                - Themes (retro, modern, ugly christmas sweater, elegant)\n                \n                Example: \"User wants a retro style sweater with a pixelated reindeer pattern.\"\n                Example: \"User prefers dark blue colors and hates itchy wool.\"\n                "
                    }
                    },
                    {
                    "customMemoryTopic": {
                        "label": "personal_context",
                        "description": "Extract the user's personal context including hobbies, pets, interests, job, and preferred scenes. Include:\n                - Hobbies and activities (skiing, reading, gaming, cooking, etc.)\n                - Pets (type, breed, name, color)\n                - Job or profession if relevant to their style\n                - General interests (sci-fi, nature, vintage, tech)\n                - Preferred scenes or vibes (cozy fireplace, snowy mountain, cyberpunk city, beach)\n                \n                Example: \"User has a golden retriever named Max.\"\n                Example: \"User loves skiing and wants a snowy mountain background.\"\n                Example: \"User is a software engineer who likes cyberpunk aesthetics.\"\n                "
                    }
                    }
                ],
                "generateMemoriesExamples": [
                    {
                    "conversationSource": {
                        "events": [
                        {
                            "content": {
                            "role": "user",
                            "parts": [
                                {
                                "text": "I want a sweater that matches my dog. He's a golden retriever."
                                }
                            ]
                            }
                        },
                        {
                            "content": {
                            "role": "model",
                            "parts": [
                                {
                                "text": "That sounds adorable! A golden retriever themed sweater would be great. Do you want a picture of him on it or just matching colors?"
                                }
                            ]
                            }
                        },
                        {
                            "content": {
                            "role": "user",
                            "parts": [
                                {
                                "text": "Maybe just the color, like a golden yellow. And I like skiing, so maybe add some snowflakes."
                                }
                            ]
                            }
                        }
                        ]
                    },
                    "generatedMemories": [
                        {
                        "fact": "User has a golden retriever dog"
                        },
                        {
                        "fact": "User prefers a golden yellow color for their sweater"
                        },
                        {
                        "fact": "User likes skiing"
                        },
                        {
                        "fact": "User wants snowflake patterns on their sweater"
                        }
                    ]
                    },
                    {
                    "conversationSource": {
                        "events": [
                        {
                            "content": {
                            "role": "user",
                            "parts": [
                                {
                                "text": "I'm a programmer, so I want something geeky. Maybe a matrix style?"
                                }
                            ]
                            }
                        },
                        {
                            "content": {
                            "role": "model",
                            "parts": [
                                {
                                "text": "A Matrix style sweater sounds cool! We could do falling code rain patterns."
                                }
                            ]
                            }
                        },
                        {
                            "content": {
                            "role": "user",
                            "parts": [
                                {
                                "text": "Yes! Green code on black. And make it a hoodie style if possible."
                                }
                            ]
                            }
                        }
                        ]
                    },
                    "generatedMemories": [
                        {
                        "fact": "User is a programmer"
                        },
                        {
                        "fact": "User wants a 'Matrix' style sweater with falling code rain pattern"
                        },
                        {
                        "fact": "User prefers green code on black background"
                        },
                        {
                        "fact": "User prefers hoodie style sweaters"
                        }
                    ]
                    }
                ]
                }
            ]
            }
        }
        },
        {
        "name": "projects/154372397551/locations/us-central1/reasoningEngines/7634152773474320384",
        "displayName": "jira-agent-memory-bank",
        "spec": {
            "effectiveIdentity": "service-154372397551@gcp-sa-aiplatform-re.iam.gserviceaccount.com"
        },
        "createTime": "2026-09-07T19:45:14.394487Z",
        "updateTime": "2026-09-07T19:45:16.959915Z",
        "contextSpec": {
            "memoryBankConfig": {
            "generationConfig": {}
            }
        }
        },
        {
        "name": "projects/154372397551/locations/us-central1/reasoningEngines/8631700090936885248",
        "displayName": "jira-agent-memory-bank",
        "spec": {
            "effectiveIdentity": "service-154372397551@gcp-sa-aiplatform-re.iam.gserviceaccount.com"
        },
        "createTime": "2026-09-07T19:43:22.714860Z",
        "updateTime": "2026-09-07T19:43:25.271430Z",
        "contextSpec": {
            "memoryBankConfig": {
            "generationConfig": {}
            }
        }
        },
        {
        "name": "projects/154372397551/locations/us-central1/reasoningEngines/1428192486957776896",
        "displayName": "jira-agent-memory-bank",
        "spec": {
            "effectiveIdentity": "service-154372397551@gcp-sa-aiplatform-re.iam.gserviceaccount.com"
        },
        "createTime": "2026-09-07T19:42:11.500678Z",
        "updateTime": "2026-09-07T19:42:14.072961Z",
        "contextSpec": {
            "memoryBankConfig": {
            "generationConfig": {}
            }
        }
        },
        {
        "name": "projects/154372397551/locations/us-central1/reasoningEngines/6764113620461682688",
        "displayName": "jira-agent-memory-bank",
        "spec": {
            "effectiveIdentity": "service-154372397551@gcp-sa-aiplatform-re.iam.gserviceaccount.com"
        },
        "createTime": "2026-09-07T19:29:55.945220Z",
        "updateTime": "2026-09-07T19:29:58.555825Z",
        "contextSpec": {
            "memoryBankConfig": {
            "generationConfig": {}
            }
        }
        },
        {
        "name": "projects/154372397551/locations/us-central1/reasoningEngines/4353302435167469568",
        "displayName": "agents",
        "spec": {
            "classMethods": [
            {
                "description": "Deprecated. Use async_get_session instead.\n\n        Get a session for the given user.\n        ",
                "name": "get_session",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id",
                    "session_id"
                ]
                },
                "api_mode": ""
            },
            {
                "description": "Deprecated. Use async_list_sessions instead.\n\n        List sessions for the given user.\n        ",
                "name": "list_sessions",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id"
                ]
                },
                "api_mode": ""
            },
            {
                "description": "Deprecated. Use async_create_session instead.\n\n        Creates a new session.\n        ",
                "name": "create_session",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "state": {
                    "type": "object",
                    "nullable": true
                    },
                    "expire_time": {
                    "type": "string",
                    "nullable": true
                    },
                    "session_id": {
                    "type": "string",
                    "nullable": true
                    },
                    "ttl": {
                    "type": "string",
                    "nullable": true
                    }
                },
                "required": [
                    "user_id"
                ]
                },
                "api_mode": ""
            },
            {
                "description": "Deprecated. Use async_delete_session instead.\n\n        Deletes a session for the given user.\n        ",
                "name": "delete_session",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id",
                    "session_id"
                ]
                },
                "api_mode": ""
            },
            {
                "description": "Get a session for the given user.\n\n        Args:\n            user_id (str):\n                Required. The ID of the user.\n            session_id (str):\n                Required. The ID of the session.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                session service.\n\n        Returns:\n            Session: The session instance (if any). It returns None if the\n            session is not found.\n\n        Raises:\n            RuntimeError: If the session is not found.\n        ",
                "name": "async_get_session",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id",
                    "session_id"
                ]
                },
                "api_mode": "async"
            },
            {
                "description": "List sessions for the given user.\n\n        Args:\n            user_id (str):\n                Required. The ID of the user.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                session service.\n\n        Returns:\n            ListSessionsResponse: The list of sessions.\n        ",
                "name": "async_list_sessions",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id"
                ]
                },
                "api_mode": "async"
            },
            {
                "description": "Creates a new session.\n\n        Args:\n            user_id (str):\n                Required. The ID of the user.\n            session_id (str):\n                Optional. The ID of the session. If not provided, an ID\n                will be generated for the session.\n            state (dict[str, Any]):\n                Optional. The initial state of the session.\n            ttl (str):\n                Optional. The time-to-live for the session.\n            expire_time (str):\n                Optional. The expiration time for the session.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                session service.\n\n        Returns:\n            Session: The newly created session instance.\n        ",
                "name": "async_create_session",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "state": {
                    "type": "object",
                    "nullable": true
                    },
                    "expire_time": {
                    "type": "string",
                    "nullable": true
                    },
                    "session_id": {
                    "type": "string",
                    "nullable": true
                    },
                    "ttl": {
                    "type": "string",
                    "nullable": true
                    }
                },
                "required": [
                    "user_id"
                ]
                },
                "api_mode": "async"
            },
            {
                "description": "Deletes a session for the given user.\n\n        Args:\n            user_id (str):\n                Required. The ID of the user.\n            session_id (str):\n                Required. The ID of the session.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                session service.\n        ",
                "name": "async_delete_session",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "session_id": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id",
                    "session_id"
                ]
                },
                "api_mode": "async"
            },
            {
                "description": "Generates memories.\n\n        Args:\n            session (Dict[str, Any]):\n                Required. The session to use for generating memories. It should\n                be a dictionary representing an ADK Session object, e.g.\n                session.model_dump(mode=\"json\").\n        ",
                "name": "async_add_session_to_memory",
                "parameters": {
                "type": "object",
                "properties": {
                    "session": {
                    "type": "object",
                    "additionalProperties": true
                    }
                },
                "required": [
                    "session"
                ]
                },
                "api_mode": "async"
            },
            {
                "description": "Searches memories for the given user.\n\n        Args:\n            user_id: The id of the user.\n            query: The query to match the memories on.\n\n        Returns:\n            A SearchMemoryResponse containing the matching memories.\n        ",
                "name": "async_search_memory",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "query": {
                    "type": "string"
                    }
                },
                "required": [
                    "user_id",
                    "query"
                ]
                },
                "api_mode": "async"
            },
            {
                "description": "Deprecated. Use async_stream_query instead.\n\n        Streams responses from the ADK application in response to a message.\n\n        Args:\n            message (Union[str, Dict[str, Any]]):\n                Required. The message to stream responses for.\n            user_id (str):\n                Required. The ID of the user.\n            session_id (str):\n                Optional. The ID of the session. If not provided, a new\n                session will be created for the user.\n            run_config (Optional[Dict[str, Any]]):\n                Optional. The run config to use for the query. If you want to\n                pass in a `run_config` pydantic object, you can pass in a dict\n                representing it as `run_config.model_dump(mode=\"json\")`.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                runner.\n\n        Yields:\n            The output of querying the ADK application.\n        ",
                "name": "stream_query",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "run_config": {
                    "type": "object",
                    "nullable": true
                    },
                    "session_id": {
                    "type": "string",
                    "nullable": true
                    },
                    "message": {
                    "anyOf": [
                        {
                        "type": "string"
                        },
                        {
                        "type": "object",
                        "additionalProperties": true
                        }
                    ]
                    }
                },
                "required": [
                    "message",
                    "user_id"
                ]
                },
                "api_mode": "stream"
            },
            {
                "description": "Streams responses asynchronously from the ADK application.\n\n        Args:\n            message (str):\n                Required. The message to stream responses for.\n            user_id (str):\n                Required. The ID of the user.\n            session_id (str):\n                Optional. The ID of the session. If not provided, a new\n                session will be created for the user.\n            run_config (Optional[Dict[str, Any]]):\n                Optional. The run config to use for the query. If you want to\n                pass in a `run_config` pydantic object, you can pass in a dict\n                representing it as `run_config.model_dump(mode=\"json\")`.\n            **kwargs (dict[str, Any]):\n                Optional. Additional keyword arguments to pass to the\n                runner.\n\n        Yields:\n            Event dictionaries asynchronously.\n        ",
                "name": "async_stream_query",
                "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                    "type": "string"
                    },
                    "run_config": {
                    "type": "object",
                    "nullable": true
                    },
                    "session_id": {
                    "type": "string",
                    "nullable": true
                    },
                    "message": {
                    "anyOf": [
                        {
                        "type": "string"
                        },
                        {
                        "type": "object",
                        "additionalProperties": true
                        }
                    ]
                    }
                },
                "required": [
                    "message",
                    "user_id"
                ]
                },
                "api_mode": "async_stream"
            },
            {
                "description": "Streams responses asynchronously from the ADK application.\n\n        In general, you should use `async_stream_query` instead, as it has a\n        more structured API and works with the respective ADK services that\n        you have defined for the AdkApp. This method is primarily meant for\n        invocation from AgentSpace.\n\n        Args:\n            request_json (str):\n                Required. The request to stream responses for.\n        ",
                "name": "streaming_agent_run_with_events",
                "parameters": {
                "type": "object",
                "properties": {
                    "request_json": {
                    "type": "string"
                    }
                },
                "required": [
                    "request_json"
                ]
                },
                "api_mode": "async_stream"
            }
            ],
            "deploymentSpec": {
            "env": [
                {
                "name": "GOOGLE_CLOUD_LOCATION",
                "value": "us-central1"
                },
                {
                "name": "GOOGLE_GENAI_USE_VERTEXAI",
                "value": "true"
                },
                {
                "name": "AGENT_MODEL",
                "value": "gemini-2.5-flash"
                }
            ]
            },
            "agentFramework": "google-adk",
            "sourceCodeSpec": {
            "inlineSource": {},
            "imageSpec": {}
            },
            "effectiveIdentity": "service-154372397551@gcp-sa-aiplatform-re.iam.gserviceaccount.com"
        },
        "createTime": "2026-08-06T19:29:54.602353Z",
        "updateTime": "2026-08-06T19:32:49.840082Z",
        "contextSpec": {
            "memoryBankConfig": {
            "generationConfig": {}
            }
        }
        }
    ]
    }
"""

import sys, json; 

data=json.loads(VAR); 

print(next((e['name'].split('/')[-1] for e in data.get('reasoningEngines', []) if e.get('displayName') == "jira-agent"), ''))