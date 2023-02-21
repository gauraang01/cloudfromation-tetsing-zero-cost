from pathlib import Path
import pytest
from cloud_radar.cf.unit import Template
import json

@pytest.fixture(scope='session')
def template_path() -> Path:
    base_path = Path(__file__).parent
    template_path = base_path / Path('../../templates/amazon-cloudformation.template.yaml')
    return template_path.resolve()

def test_params(template_path: Path):
    template = Template.from_yaml(template_path)
    region = "us-west-2"
    EksClusterName = "cf-testing"

    # Dictionary Of Parameters
    params = {"EksClusterName":EksClusterName}

   # Render the template using parameters and region
    result = template.render(params, region)

   # Print template
    print(json.dumps(result, indent=4, default=str))

   # Check if Proper resources have been created
    resource_list = ["MetricsServer"]
    for resource in resource_list:
        assert resource in result["Resources"]

    # Test Metrics Server
    MetricsServer_resource = result["Resources"]['MetricsServer']['Properties']
    assert "cf-testing" == MetricsServer_resource['ClusterName']

    #Test Outputs

    outputs = result['Outputs']
    assert "MetricsServer" == outputs['MetricsServer']['Value']
