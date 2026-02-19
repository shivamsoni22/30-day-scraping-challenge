# 30-day-scraping-challenge

30 days self challenge to scrape 30 websites using Python with full pagination, raw HTML saving, structured CSV output, and clean Git workflow without using proxies or scraping APIs.



\## Day 2 - preisportal.pique-ferry.de



Platform URL:

https://preisportal.pique-ferry.de/



Objective:

Attempted to analyze and scrape pricing data from the platform.



Technical Analysis \& Findings:



\- The platform uses authenticated session-based access.

\- Direct HTTP requests return unauthorized or restricted responses.

\- Dynamic request validation mechanisms detected.

\- Strong anti-bot filtering blocks automated scraping attempts.

\- Network inspection indicates controlled access to pricing endpoints.

\- Rate-limiting and request validation tokens observed.

\- Access appears restricted to authorized internal or partner users.



Challenges Faced:



\- No publicly accessible API endpoints.

\- Browser session cookies required for data visibility.

\- Automated requests flagged and blocked.

\- Security headers and validation checks prevent standard scraping methods.



Conclusion:



Scraping this platform using traditional methods (requests, BeautifulSoup, simple automation) is not feasible due to authentication controls and anti-bot protections.



Further exploration would require:



\- Authenticated session handling

\- Advanced browser automation (Selenium/Playwright)

\- Proper access credentials

\- Ethical and legal compliance review



