from .responses import CloudFormationResponse

url_bases = [
    "https?://cloudformation.(.+).amazonaws.com",
]

url_paths = {
    '{0}/$': CloudFormationResponse().dispatch,
}
