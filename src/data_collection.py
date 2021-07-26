import os
import snscrape


class ScrapeTweets:

    def run_snscrape_twitter_stream_job(self, hashtag, limit=500):
        try:
            os.system(
                'snscrape --jsonl --max-results {} twitter-hashtag {} > ../data/hashtag-{}-tweets.json'.format(limit,
                                                                                                               hashtag,
                                                                                                               hashtag))
        except:
            print('CLI command failure..')

    def run_snscrape_twitter_profile_job(self, userName, limit=100):
        try:
            os.system(
                'snscrape --jsonl --max-results {} twitter-search "from:{}" > ../data/user-tweets-{}.json'.format(limit,
                                                                                                                  userName,
                                                                                                                  userName))
        except:
            print('CLI command failure..')

    def run_snscrape_twitter_text_search_query_job(self, since, until, textQuery, limit=100):
        """Scrape tweets with a search query

        Args:
            since (date: yyyy-mm-dd): Start date
            until (date: yyyy-mm-dd): end date
            textQuery (str): text query for twitter search
            limit (int, optional): No of tweets to scrape. Defaults to 100.
        """
        try:
            os.system(
                'snscrape --jsonl --max-results {} --since {} twitter-search "{} until:{}" > ../data/text-query-tweets-{}.json'.format(
                    limit, since, textQuery, until, textQuery))
        except:
            print('CLI command failure..')


if __name__ == '__main__':
    pass
    print('all done')
    # classObj = ScrapeTweets()
    # classObj.run_snscrape_twitter_stream_job('nlproc', 1000)