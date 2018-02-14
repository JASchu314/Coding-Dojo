select sum(amount) as total_revenue from billing
where year(charged_datetime)=2012 and month(charged_datetime)= 3;

select sum(amount) as total_revenue from billing
join clients
on billing.client_id = clients.client_id
where clients.client_id = 2;

select * from sites
join clients
on clients.client_id = sites.client_id
where clients.client_id = 10;

select sites.site_id, count(sites.site_id) as number_of_websites, month(sites.created_datetime), year(sites.created_datetime) from sites
join clients
on clients.client_id = sites.client_id
where clients.client_id = 1
group by sites.created_datetime;

select sites.domain_name, count(leads.leads_id) as num_leads, leads.registered_datetime from sites
join leads 
on sites.site_id = leads.site_id
where leads.registered_datetime between cast('2011-01-01' as date) and cast('2011-02-15' as date) 
group by sites.domain_name;

select clients.first_name, count(leads.leads_id) as number_of_leads from sites
join clients
on clients.client_id = sites.client_id
join leads
on leads.site_id = sites.site_id
where leads.registered_datetime between cast('2011-1-1' as date) and cast('2011-12-31' as date)
group by clients.first_name;

select concat_ws(' ', clients.first_name, clients.last_name) as client_name, count(leads.leads_id) as number_of_leads, monthname(leads.registered_datetime) as month_generated from sites
join clients
on clients.client_id = sites.client_id
join leads
on leads.site_id = sites.site_id
where leads.registered_datetime between cast('2011-1-1' as date) and cast('2011-06-30' as date)
group by client_name, month_generated; 

select concat_ws(' ', clients.first_name, clients.last_name) as client_name, sites.domain_name, count(leads.leads_id) as number_of_leads, date_format(leads.registered_datetime, '%M %d, %Y') as date_generated from sites
join clients
on clients.client_id = sites.client_id
join leads
on leads.site_id = sites.site_id
where leads.registered_datetime between cast('2011-1-1' as date) and cast('2011-12-31' as date)
group by clients.client_id;

select concat_ws(' ',clients.first_name, clients.last_name) as client_name, sum(amount) as total_revenue, monthname(billing.charged_datetime) as month_charged, year(billing.charged_datetime) as year_charged from billing
join clients
on billing.client_id = clients.client_id
group by month_charged, clients.client_id, year_charged
order by clients.client_id, year_charged, month(billing.charged_datetime);

select concat_ws(' ', clients.first_name, clients.last_name) as client_name, group_concat(sites.domain_name separator ' /') as domains from clients
join sites on sites.client_id = clients.client_id
group by client_name
order by clients.client_id;

