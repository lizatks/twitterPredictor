from twitterPredictor.twitter_collect.collect import *


def  extract_max_rt(query) :
    data = collect_to_pandas_dataframe(query)
    rt_max  = np.max(data['RTs'])
    rt  = data[data.RTs == rt_max].index[0]

    # Max RTs:
    print("The tweet with more retweets is: \n{}".format(data['tweet_textual_content'][rt]))
    print("Number of retweets: {}".format(rt_max))
    print("{} characters.\n".format(data['len'][rt]))

