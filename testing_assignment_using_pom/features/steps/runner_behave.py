import os
import utils
from pathlib import Path
from dotenv import load_dotenv
from behave.__main__ import run_behave
from behave.configuration import Configuration
from behave.tag_expression import TagExpression

def main():

    load_dotenv()
    my_details=os.getenv("ENVIRONMENT")
    print(my_details)


    reports = "C://Users//a98016117//PycharmProjects//Updated_POM_Task//testing_assignment_using_pom" +"/"+ os.getenv("REPORTS_FOLDER")
    reports = os.path.normpath(f'"{reports}"')

    feature_order = '" "'.join(
        os.path.join("C://Users//a98016117//PycharmProjects//Updated_POM_Task//testing_assignment_using_pom", feature_path.strip())
        for feature_path in os.getenv("FEATURE_ORDER").split(",")
        if Path("C://Users//a98016117//PycharmProjects//Updated_POM_Task//testing_assignment_using_pom" +"/"+ feature_path.strip()).exists()
    )
    feature_order = os.path.normpath(f'"{feature_order}"')
    print(feature_order)

    arguments = (
        f"{feature_order} -f allure_behave.formatter:AllureFormatter -o {reports}"
        # f"{stop_fail} --no-skipped -f plain {tags_option} --no-capture "
        # f"--no-capture-stderr --no-logcapture "
    )

    print(arguments)
    # log.error(arguments)
    configuration = Configuration(arguments)

    for i in range(1):
        run_behave(configuration)


if __name__ == "__main__":
    main()
