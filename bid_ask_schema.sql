create table bid_ask (
    id  integer primary key autoincrement not null,
    bid_ask_value text,
    source text,
    timestamp date
);