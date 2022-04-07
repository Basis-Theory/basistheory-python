# Token

## Properties

Name | Type | Description |
------------ | ------------- | -------------
**id** | **str** | Unique identifier of the token which can be used to get a token
**type** | **str** | Token type
**tenant_id** | **str** | The Tenant ID which owns the token
**data** | **bool, date, datetime, dict, float, int, list, str, none_type** | Token data
**metadata** | **{str: (str,)}** | A key-value map of non-sensitive data
**encryption** | [**EncryptionMetadata**](EncryptionMetadata.md) | Encryption metadata for an encrypted token data value
**created_by** | **str, none_type** | (Optional) The Application ID which created the token
**created_at** | **datetime, none_type** | (Optional) Created date of the token in ISO 8601 format
**modified_by** | **str, none_type** | (Optional) The Application ID which last modified the token
**modified_at** | **datetime, none_type** | (Optional) Last modified date of the token in ISO 8601 format
**children** | [**[Token]**](Token.md) | Array of child tokens where this token is the parent in an association
**fingerprint** | **str** | Uniquely identifies the contents of this token. Fingerprints are only available for Card and Bank token types.

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
