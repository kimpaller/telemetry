def url_gen(
        jenkins_server,
        jenkins_port,
        project_name, 
        build_number, 
        board,
        hdl_commit='NA',
        linux_commit='NA'
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
    if not hdl_commit=='NA':
        url_hdl_commit = 'https://github.com/analogdevicesinc/hdl/commits/{}'.format(
                                hdl_commit
                            )
    else:
        url_hdl_commit = 'NA'

    if not linux_commit=='NA':
        url_linux_commit = 'https://github.com/analogdevicesinc/linux/commits/{}'.format(
                                linux_commit
                            )
    else:
        url_linux_commit= 'NA'

    return {
        'Jenkins Project Name': url_project_name,
        'Jenkins Build Number': url_build_number,
        'pyadi Tests': url_pytest_report,
        'Linux Tests': url_artifacts,
        'HDL Commit': url_hdl_commit,
        'Linux Commit': url_linux_commit
    }


if __name__ == "__main__":
    print(url_gen('10.116.171.86',
                  '8080',
                  'HW_tests/HW_test_multiconfig',
                  '137',
                  'zynq_zed_adv7511_ad9364_fmcomms4'
                ))