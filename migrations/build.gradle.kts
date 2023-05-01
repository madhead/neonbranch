import java.lang.System.getenv as env

plugins {
    alias(libs.plugins.liquibase)
}

dependencies {
    liquibaseRuntime(libs.liquibase.core)
    liquibaseRuntime(libs.picocli)
    liquibaseRuntime(libs.postgresql)
}

liquibase {
    activities {
        register("neonbranch") {
            this.arguments = mapOf(
                "driver" to "org.postgresql.Driver",

                "url" to "jdbc:postgresql://${env("NEON_HOST")}/${env("NEON_DATABASE")}",
                "username" to env("NEON_USER"),
                "password" to env("NEON_PASSWORD"),

                "searchPath" to project.projectDir,
                "changelogFile" to "src/main/liquibase/changelog.yml"
            )
        }
    }
}
