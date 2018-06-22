"""
@Project   : ssr_url_parser
@Module    : parse_ssr_url.py
@Author    : tyong920 [tyong920@gmail.com]
@Created   : 2018/6/22 16:52
@Desc      : 
"""
import click

from ssr_url_parser import parse_ssr_url, ParseError


@click.command()
@click.argument('ssr_url')
def cli(ssr_url):
    try:
        parsed = parse_ssr_url(ssr_url)
    except ParseError:
        click.echo('Parse failed. Please enter a valid ssr url.')
    else:
        click.echo(parsed)


if __name__ == '__main__':
    cli()
