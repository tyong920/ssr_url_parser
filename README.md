# ssr_url_parser
A tiny CLI tool for parsing SSR url to plain text.

1. **Installation**:
   - Use pip
       ```bash
       pip install ssr-url-parser
       ```

2. **Usage**:
    - If you  want to use it in terminal.
        ```bash
        ssr-parse "ssr://a-valid-ssr-url-......"
        ```
    - If you want to parse the ssr url in your own application.
        ```python
        from ssr_url_parser import parse_ssr_url
        
        parsed = parse_ssr_url("ssr://a-valid-ssr-url-......")
        ```

