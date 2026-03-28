from django.http import HttpResponse


def home(request):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Banking API</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 800px; margin: 50px auto; padding: 0 20px; }
            h1 { color: #2c3e50; }
            h2 { color: #34495e; border-bottom: 1px solid #eee; padding-bottom: 8px; }
            table { width: 100%; border-collapse: collapse; margin-bottom: 20px; }
            th { background: #2c3e50; color: white; padding: 10px; text-align: left; }
            td { padding: 8px 10px; border-bottom: 1px solid #eee; }
            tr:hover { background: #f5f5f5; }
            .badge { background: #27ae60; color: white; padding: 2px 8px; border-radius: 4px; font-size: 12px; }
            .badge.get { background: #2980b9; }
            .badge.delete { background: #e74c3c; }
            a.swagger-btn { display: inline-block; background: #27ae60; color: white; padding: 12px 24px; border-radius: 6px; text-decoration: none; font-weight: bold; margin-top: 10px; }
            a.swagger-btn:hover { background: #219a52; }
            code { background: #f4f4f4; padding: 2px 6px; border-radius: 4px; }
        </style>
    </head>
    <body>
        <h1>Banking API</h1>
        <p>A PayPal-style banking API built with Django REST Framework. Supports user authentication, account management, and secure money transfers.</p>

        <a class="swagger-btn" href="/swagger/">Open Swagger UI</a>

        <h2>Authentication</h2>
        <table>
            <tr><th>Method</th><th>Endpoint</th><th>Description</th></tr>
            <tr><td><span class="badge">POST</span></td><td><code>/api/auth/register/</code></td><td>Register new user</td></tr>
            <tr><td><span class="badge">POST</span></td><td><code>/api/auth/login/</code></td><td>Login and get JWT tokens</td></tr>
            <tr><td><span class="badge">POST</span></td><td><code>/api/auth/refresh/</code></td><td>Refresh access token</td></tr>
            <tr><td><span class="badge get">GET</span></td><td><code>/api/auth/me/</code></td><td>Get current user profile</td></tr>
            <tr><td><span class="badge">PUT</span></td><td><code>/api/auth/me/</code></td><td>Update profile</td></tr>
        </table>

        <h2>Accounts</h2>
        <table>
            <tr><th>Method</th><th>Endpoint</th><th>Description</th></tr>
            <tr><td><span class="badge">POST</span></td><td><code>/api/accounts/create/</code></td><td>Create account</td></tr>
            <tr><td><span class="badge get">GET</span></td><td><code>/api/accounts/</code></td><td>List my accounts</td></tr>
            <tr><td><span class="badge get">GET</span></td><td><code>/api/accounts/&lt;id&gt;/</code></td><td>Account detail</td></tr>
            <tr><td><span class="badge delete">DELETE</span></td><td><code>/api/accounts/&lt;id&gt;/</code></td><td>Deactivate account</td></tr>
        </table>

        <h2>Transactions</h2>
        <table>
            <tr><th>Method</th><th>Endpoint</th><th>Description</th></tr>
            <tr><td><span class="badge">POST</span></td><td><code>/api/transactions/transfer/</code></td><td>Transfer money by email</td></tr>
            <tr><td><span class="badge get">GET</span></td><td><code>/api/transactions/</code></td><td>List transactions</td></tr>
            <tr><td><span class="badge get">GET</span></td><td><code>/api/transactions/&lt;id&gt;/</code></td><td>Transaction detail</td></tr>
        </table>

        <h2>Security</h2>
        <ul>
            <li>JWT tokens expire after 1 hour</li>
            <li>Refresh tokens expire after 7 days</li>
            <li>All transfers use atomic transactions with row-level locking</li>
            <li>Balances can never go negative</li>
        </ul>
    </body>
    </html>
    """
    return HttpResponse(html)
