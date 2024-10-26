import os
import sys
from pyairtable import Api


def main(grade, pytest_output_string, pylint_score):

    print("start updating db")

    # get environment variables

    github_workspace = os.environ['GITHUB_WORKSPACE']
    runner_workspace = os.environ['RUNNER_WORKSPACE']
    github_workflow = os.environ['GITHUB_WORKFLOW']
    github_workflow_ref = os.environ['GITHUB_WORKFLOW_REF']
    github_workflow_sha = os.environ['GITHUB_WORKFLOW_SHA']
    github_sha = os.environ['GITHUB_SHA']
    github_job = os.environ['GITHUB_JOB']
    github_action = os.environ['GITHUB_ACTION']
    github_run_id = os.environ['GITHUB_RUN_ID']
    github_run_number = os.environ['GITHUB_RUN_NUMBER']
    github_run_attempt = os.environ['GITHUB_RUN_ATTEMPT']
    github_triggering_actor = os.environ['GITHUB_TRIGGERING_ACTOR']
    github_actor = os.environ['GITHUB_ACTOR']
    github_actor_id = os.environ['GITHUB_ACTOR_ID']
    github_repository = os.environ['GITHUB_REPOSITORY']
    github_repository_id = os.environ['GITHUB_REPOSITORY_ID']
    github_repository_owner = os.environ['GITHUB_REPOSITORY_OWNER']
    github_repository_owner_id = os.environ['GITHUB_REPOSITORY_OWNER_ID']

    airtable_pat = os.environ['AIRTABLE_PAT']
    db_id = os.environ['AIRTABLE_DB_ID']
    table_id = os.environ['AIRTABLE_TABLE_ID']

    print(f'{github_workspace=}')
    print(f'{runner_workspace=}')
    print(f'{github_workflow=}')
    print(f'{github_workflow_ref=}')
    print(f'{github_workflow_sha=}')
    print(f'{github_sha=}')
    print(f'{github_job=}')
    print(f'{github_action=}')
    print(f'{github_run_id=}')
    print(f'{github_run_number=}')
    print(f'{github_run_attempt=}')
    print(f'{github_triggering_actor=}')
    print(f'{github_actor=}')
    print(f'{github_actor_id=}')
    print(f'{github_repository=}')
    print(f'{github_repository_id=}')
    print(f'{github_repository_owner=}')
    print(f'{github_repository_owner_id=}')

    data = {
    'actor' : github_actor,
    'pylint': pylint_score,
    'grade' : grade,
    'string' : pytest_output_string,
    'sha' : github_sha,
    'run_number' : github_run_number,
    'repository' : github_repository,
    }

    try:
        api = Api(airtable_pat)
        table = api.table(db_id, table_id)
        response = table.create(data)
        print('Record inserted:', response)
    except Exception as e:
        print(e)
        sys.exit(1)

    print("end updating db")


if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: python updatedb.py grade pytest_output_string pylint_score")
        sys.exit(1)

    main(float(sys.argv[1]), sys.argv[2], float(sys.argv[3]))
