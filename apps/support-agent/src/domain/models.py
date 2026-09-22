"""Domain models for the Sunrise support agent.

The source of truth for our data shapes. Money is rupees as int (amount_inr,
price_inr); dates are datetime.date. Fields match the canon in CLAUDE.md and
_memory/solution/dataModel.md.
"""

from datetime import date

from pydantic import BaseModel


class Product(BaseModel):
    sku: str
    name: str
    category: str
    price_inr: int
    warranty_months: int


class PolicyDoc(BaseModel):
    doc_id: str
    title: str
    version: str
    region: str
    effective_date: date
    body_markdown: str


class FaqItem(BaseModel):
    faq_id: str
    question: str
    answer: str
    topic: str


class Order(BaseModel):
    order_id: str
    customer_name: str
    city: str
    sku: str
    amount_inr: int
    promised_date: date
    delivery_date: date | None = None
    status: str


class Ticket(BaseModel):
    ticket_id: str
    intent: str
    message: str
    resolution: str | None = None


class EvalCase(BaseModel):
    case_id: str
    question: str
    expected_passages: list[str]
    ground_truth: str
    expected_tools: list[str]
    should_escalate: bool
    tags: list[str]
