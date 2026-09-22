# Data model

Home: apps/support-agent/src/domain/models.py (the source of truth).
Status: finalized in code (Module 4). Pydantic BaseModel classes; money as int rupees
(price_inr, amount_inr); dates as datetime.date. Optional in code: Order.delivery_date
and Ticket.resolution default to None (open/undelivered).

## Entities (key fields)
- Product: sku, name, category, price_inr, warranty_months
- PolicyDoc: doc_id, title, version, region, effective_date, body_markdown
- FaqItem: faq_id, question, answer, topic
- Order: order_id, customer_name, city, sku, amount_inr, promised_date, delivery_date, status
- Ticket: ticket_id, intent, message, resolution
- EvalCase: case_id, question, expected_passages, ground_truth, expected_tools, should_escalate, tags

## Canon rows
- Order SE-4021: Pune, promised 2026-09-05, delivered 2026-09-09, status late, amount 9999.

## Where the data lives (paths from the base)
- data/knowledge/ (documents), data/generated/sunrise.duckdb (orders), data/generated/ (generated JSON), data/eval/ (golden eval set).
