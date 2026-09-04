from client import FullstackEnvVariableDriftResolverClient

def main():
    client = FullstackEnvVariableDriftResolverClient()
    res = client.audit_and_sync_env_vars()
    print('Env Drift Resolver: ' + res['env_audit_id'] + ' (Client: ' + str(res['client_keys_count']) + ' | Backend: ' + str(res['backend_keys_count']) + ')')
    print('Leaks: ' + str(res['insecure_client_leaks']) + ' | Template Valid: ' + str(res['env_example_template_generated']))
    print('Audit URL: ' + res['drift_audit_report_url'])

if __name__ == '__main__':
    main()
