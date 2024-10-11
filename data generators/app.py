import customer_test_data as cust
import transactions_test_data as transactions
import transaction_item_test_data as trans_item
import product_test_data as product
import interaction_test_data as inter_data
import marketing_campaign_test_data as campaigns
import campain_result_test_data as campaign_results
import digital_engagement_data as digital_engagement
import social_media_interaction_test_data as soc_med_interactions
import product_review_test_data as prod_reviews
import customer_feedback_test_data as cust_feedback
import omnichannel_journey_test_data as omnichannel_journey
import price_history_test_data as price_history
import promotions_test_data as promotions
import inventory_log_test_data as inventory_logs
import fulfillment_test_data as fulfillments
import local_event_test_data as local_events
import competitor_activity_test_data as competitor_activities
import industry_trends_test_data as industry_trends
import csv
import os
import random

# change cwd to test data
os.chdir('static/test data/data files')

# create a file object to write data to
def write_to_file(filename, header, content):
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(content)

cust.generate_customer_data(1000)
write_to_file('customers.csv', cust.customer_header, cust.customers)

transactions.generate_transaction_data(5000)
for transaction in transactions.transactions:
    transaction['customer_id'] = (random.choice(cust.customers)['customer_id']) # create the foreign key
write_to_file('transactions.csv', transactions.transaction_header, transactions.transactions)
    
product.generate_product_data(100)
write_to_file('products.csv', product.product_header, product.products)

trans_item.generate_transaction_item_data(15000)
for transaction_item in trans_item.transaciton_items:
    transaction_item['transaction_id'] = (random.choice(transactions.transactions)['transaction_id']) # create the foreign key
    transaction_item['product_id'] = (random.choice(product.products)['product_id']) # create the foreign key
write_to_file('transaction_items.csv', trans_item.transaction_item_header, trans_item.transaciton_items)

inter_data.generate_interactions(50000)
for interaction in inter_data.interactions:
    interaction['customer_id'] = (random.choice(cust.customers)['customer_id']) # create the foreign key    
write_to_file('interactions.csv', inter_data.interaction_header, inter_data.interactions)

campaigns.generate_campaign_data(20)
write_to_file('marketing_campaigns.csv', campaigns.campaign_header, campaigns.campaigns)

campaign_results.generate_campaign_results(500)
for campaign_result in campaign_results.campaign_results:
    campaign_result['campaign_id'] = (random.choice(campaigns.campaigns)['campaign_id']) # create the foreign key
    campaign_result['customer_id'] = (random.choice(cust.customers)['customer_id']) # create the foreign key
write_to_file('campaign_results.csv', campaign_results.campaign_results_header, campaign_results.campaign_results)

digital_engagement.generate_digital_engagement_data(50000)
for engagement in digital_engagement.engagements:
    engagement['customer_id'] = (random.choice(cust.customers)['customer_id']) # create the foreign key
write_to_file('digital_engagement.csv', digital_engagement.engagements_header, digital_engagement.engagements)
    
soc_med_interactions.generate_soc_med_interactions(10000)
for interaction in soc_med_interactions.soc_med_interactions:
    interaction['customer_id'] = (random.choice(cust.customers)['customer_id']) # create the foreign key
write_to_file('social_media_interactions.csv', soc_med_interactions.soc_med_interactions_header, soc_med_interactions.soc_med_interactions)

prod_reviews.generate_product_reviews(100000)
for review in prod_reviews.prod_reviews:
    review['customer_id'] = (random.choice(cust.customers)['customer_id']) # create the foreign key
    review['product_id'] = (random.choice(product.products)['product_id']) # create the foreign key
write_to_file('product_reviews.csv', prod_reviews.prod_reviews_header, prod_reviews.prod_reviews)

cust_feedback.generate_feedback_data(100000)
for feedback in cust_feedback.feedback:
    feedback['customer_id'] = (random.choice(cust.customers)['customer_id']) # create the foreign key
write_to_file('customer_feedback.csv', cust_feedback.feedback_header, cust_feedback.feedback)

omnichannel_journey.generate_omnichanel_journey_data(200000)
for journey in omnichannel_journey.journeys:
    journey['customer_id'] = (random.choice(cust.customers)['customer_id']) # create the foreign key
write_to_file('omnichannel_journey.csv', omnichannel_journey.journeys_header, omnichannel_journey.journeys)

promotions.generate_promotions(100)
write_to_file('promotions.csv', promotions.promotions_header, promotions.promotions)

price_history.generate_price_history(100)
for history in price_history.history:
    history['product_id'] = (random.choice(product.products)['product_id']) # create the foreign key
    history['promotion_id'] = (random.choice(promotions.promotions)['promotion_id']) # create the foreign key
write_to_file('price_history.csv', price_history.history_header, price_history.history)

inventory_logs.generate_logs(250000)
for log in inventory_logs.logs:
    log['product_id'] = (random.choice(product.products)['product_id']) # create the foreign key
write_to_file('inventory_logs.csv', inventory_logs.log_header, inventory_logs.logs)

fulfillments.generate_fulfillments(10000)
for fulfillment in fulfillments.fulfillments:
    fulfillment['order_id'] = (random.choice(transactions.transactions)['transaction_id']) # create the foreign key
write_to_file('fulfillments.csv', fulfillments.fulfillment_header, fulfillments.fulfillments)

local_events.generate_local_event_data(50)
write_to_file('local_events.csv', local_events.events_header, local_events.events)

competitor_activities.generate_competitior_activity_data(25)
write_to_file('competitor_activities.csv', competitor_activities.activities_header, competitor_activities.activities)

industry_trends.generate_trend_data(100)
write_to_file('industry_trends.csv', industry_trends.trends_header, industry_trends.trends)


