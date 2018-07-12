package jenkins_jobs.support

import javaposse.jobdsl.dsl.JobParent
import javaposse.jobdsl.dsl.MemoryJobManagement

class MockJobParent extends JobParent {

    MockJobParent() {
        setJm new MemoryJobManagement()
    }

    @Override
    Object run() {
        return null
    }
}
