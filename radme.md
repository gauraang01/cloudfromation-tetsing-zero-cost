# Project Title:
AWS CloudFormation Testing pipeline at zero cost

# Problem Staement
In cloud-based working environments, deploying AWS CloudFormation templates without proper testing can lead to failures
in the infrastructure. While testing tools like TaskCat ensure proper functionality of templates, the high cost of
deploying new resources to multiple regions during testing presents a significant challenge. A solution is needed to
effectively test CloudFormation templates without incurring significant costs to minimize production issues and infrastructure downtime.

# Project Description:
This project proposes a solution to test AWS CloudFormation templates in a CI/CD pipeline using open-source tools.
The solution consists of various phases that perform different types of testing, including linting, security testing,
policy testing, unit testing, and functional testing. The goal is to ensure that the templates are properly functional
and do not incur high costs in the production environment.

One solution is to use open-source tools like cfn-lint, cfn-nag, cfn-guard, and cloud-radar to perform various types of testing,
including linting, security testing, policy testing, unit testing, and functional testing. To ensure that all of these tools are
used consistently across the codebase, pre-commit hooks can be used.

Pre-commit is a tool that allows you to specify various hooks, which are run automatically before you commit your code.
These hooks check your code against a set of predefined rules to ensure that it meets certain standards before it is committed.
In this case, pre-commit can be configured to run all the necessary testing tools, including cfn-lint, cfn-nag, cfn-guard, and cloud-radar,
before the code is committed to the repository. This helps to ensure that the CloudFormation templates are properly tested and adhere to best practices,
which in turn reduces the likelihood of failures in the production environment.

By using pre-commit hooks, developers can ensure that their code is thoroughly tested before it is committed to the repository,
which can reduce the risk of issues arising in the production environment. This approach also helps to promote consistency across
the codebase and ensures that all CloudFormation templates are tested in the same way, regardless of who wrote them.

## Phases of the proposed solution:
### Phase-1
Setting up the environment
In this phase, the environment is set up for the testing pipeline.
This includes creating a venv, setting up the required permissions, and installing the necessary tools.

### Phase-2
Static code Analysis
* Linting using cfn-lint
* Security testing using cfn-nag
* Policy and rule testing using cfn-guard
Linting is used to ensure that the templates are following the best practices, while security and policy
testing is performed to detect any vulnerabilities or non-compliance issues.

### Phase-3
Unit testing using cloud-radar
This tool is used to perform unit tests on the templates to check if they are functioning as expected.

### Phase-4
Deploying to localstack
 In this phase, the templates are deployed to localstack, which is a local AWS cloud environment.
 This is done to test the templates in an environment similar to the production environment without incurring high costs.

### Phase-5
Improving efficiency by using Github action
This phase includes integrating the testing pipeline with Github actions. This will automate the testing process,
and the templates will be tested automatically whenever a new commit is pushed to the repository.

# Directory structure

mkdir templates
mkdir tests
mkdir tests/unit

* Templates directory will store cloud formation templates
* Tests/unit directory will store unit tests


# Setup
1. Create a virtual environment and activate it using the following commands
```bash
python3.9 -m venv ev
source ev/bin/activate
```

2. Install required modules using:
```bash
pip install -r requirements.txt
```


3. Initialize as a git repository
```bash
git init
```

4. Select a Cloud Formation template for demonstration: amazon-cloudformation.template.yaml and pastes its content in a file in the templates directory

5. Run pre-commit using the following command:
```bash
pre-commit install
```

7. To run all the tests cases:
```bash
pre-commit run
```
