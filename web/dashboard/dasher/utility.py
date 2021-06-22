def url_gen(
        jenkins_server,
        jenkins_port,
        project_name, 
        build_number, 
        board
    ):
    ''' Utility method for generating urls'''

    url_project_name = 'http://{}:{}/job/{}/'.format(
                            jenkins_server,
                            jenkins_port,
                            project_name.replace('/','/job/')
                        )

    url_build_number = 'http://{}:{}/job/{}/{}/'.format(
                            jenkins_server,
                            jenkins_port,
                            project_name.replace('/','/job/'),
                            build_number
                        )

    url_pytest_report = 'http://{}:{}/job/{}/{}/{}/'.format(
                            jenkins_server,
                            jenkins_port,
                            project_name.replace('/','/job/'),
                            build_number,
                            board.replace('-','_')
                        )
    url_artifacts = 'http://{}:{}/job/{}/{}/artifact/dmesg_{}_err.log'.format(
                            jenkins_server,
                            jenkins_port,
                            project_name.replace('/','/job/'),
                            build_number,
                            board
                        )

    return {
        'Jenkins Project Name': url_project_name,
        'Jenkins Build Number': url_build_number,
        'pyadi Tests': url_pytest_report,
        'Linux Tests': url_artifacts
    }


if __name__ == "__main__":
    print(url_gen('10.116.171.86',
                  '8080',
                  'HW_tests/HW_test_multiconfig',
                  '137',
                  'zynq_zed_adv7511_ad9364_fmcomms4'
                ))