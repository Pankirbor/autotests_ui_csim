from playwright.sync_api import Page, Request, Route


def add_coverage_script(page: Page):
    """Динамически добавляет скрипт UI Coverage в html."""

    def inject_coverage_script(route: Route, request: Request):
        if not request.resource_type == "document":
            route.continue_()
            return

        response = route.fetch()

        content_type = response.headers.get("content-type", "")
        if "text/html" not in content_type:
            route.continue_()
            return

        html_content = response.text()
        modified_html_content = html_content.replace(
            "</body>",
            "<script src='https://nikita-filonov.github.io/ui-coverage-report/agent.global.js'></script></body>",
        )
        route.fulfill(
            status=response.status,
            headers=response.headers,
            body=modified_html_content.encode("utf-8"),
            content_type="text/html",
        )
        page.route("**/*", inject_coverage_script)
