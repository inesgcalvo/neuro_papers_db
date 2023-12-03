import re



def extraer_informacion(x):
    """
    Extracts information from a given input string following a specific format.

    Parameters:
    - x (str): Input string containing structured information.

    Returns:
    dict: A dictionary containing extracted information with keys such as 'PMID', 'OWN', 'STAT', etc.
          The values associated with these keys are the extracted data from the input string.

    Note:
    The function uses regular expressions to search for specific patterns in the input string (x)
    and extracts relevant information based on those patterns.
    """
    info = {}

    match_pmid = re.search(r'PMID- (\d+)', x)
    if match_pmid:
        info['ID'] = match_pmid.group(1)
    
    match_own = re.search(r'OWN - (\w+)', x)
    if match_own:
        info['ownership'] = match_own.group(1)
        
    match_stat = re.search(r'STAT- (\w+)', x)
    if match_stat:
        info['status'] = match_stat.group(1)
    
    match_dcom = re.search(r'DCOM- (\d+)', x)
    if match_dcom:
        info['completion_date'] = match_dcom.group(1)
    
    match_lr = re.search(r'LR  - (\d+)', x)
    if match_lr:
        info['last_revision'] = match_lr.group(1)
    
    match_is = re.findall(r'IS  - (.+)', x)
    if match_is:
        info['ISSN'] = match_is
    
    match_vi = re.search(r'VI  - (\d+)', x)
    if match_vi:
        info['volume'] = match_vi.group(1)
        
    match_ip = re.search(r'IP  - (\d+)', x)
    if match_ip:
        info['issue'] = match_ip.group(1)
    
    match_dp = re.search(r'DP  - (.+)', x)
    if match_dp:
        info['publication_date'] = match_dp.group(1)
    
    match_ti = re.search(r'TI  - (.+)', x)
    if match_ti:
        info['title'] = match_ti.group(1)
    
    match_pg = re.search(r'PG  - (.+)', x)
    if match_pg:
        info['pages'] = match_pg.group(1)
        
    match_lid = re.search(r'LID - (\S+)', x)
    if match_lid:
        info['DOI'] = match_lid.group(1)
           
    match_authors = re.findall(r'FAU - (.+)', x)
    if match_authors:
        info['authors'] = match_authors
        info['first_auth'] = match_authors[0]
        info['last_auth'] = match_authors[-1]
        
    match_auid = re.findall(r'AUID- (.+)', x)
    if match_auid:
        info['first_auth_ID'] = match_auid[0]
        info['last_auth_ID'] = match_auid[-1]
        
    match_auaff = re.findall(r'AD  - (.+)', x)
    if match_auaff:
        info['auth_aff_list'] = match_auaff
        info['first_auth_aff'] = match_auaff[0]
        info['last_auth_aff'] = match_auaff[-1]
    
    match_jrabb = re.search(r'TA  - (.+)', x)
    if match_jrabb:
        info['journal_abb'] = match_jrabb.group(1)
    
    match_journal = re.search(r'JT  - (.+)', x)
    if match_journal:
        info['journal'] = match_journal.group(1)
        
    match_ot = re.findall(r'OT  - (.+)', x)
    if match_ot:
        info['other_terms'] = match_ot

    match_ci = re.search(r'CI  - (.+)', x)
    if match_ci:
        info['copyright_information'] = match_ci.group(1)

    match_abstract = re.search(r'AB  - (.+)', x)
    if match_abstract:
        info['abstract'] = match_abstract.group(1)
    
    match_lang = re.search(r'LA  - (.+)', x)
    if match_lang:
        info['lang'] = match_lang.group(1)
        
    match_pub = re.search(r'PT  - (.+)', x)
    if match_pub:
        info['pub_type'] = match_pub.group(1)
        
    match_jid = re.search(r'JID - (\d+)', x)
    if match_jid:
        info['journal_ID'] = match_jid.group(1)

    match_rn = re.search(r'RN  - (.+)', x)
    if match_rn:
        info['registry_num'] = match_rn.group(1)

    match_sb = re.search(r'SB  - (.+)', x)
    if match_sb:
        info['source_pub'] = match_sb.group(1)

    match_mh = re.findall(r'MH  - (.+)', x)
    if match_mh:
        info['MeSH_terms'] = match_mh

    match_pmc = re.search(r'PMC - (\w+)', x)
    if match_pmc:
        info['pubmed_central_ID'] = match_pmc.group(1)

    match_cois = re.search(r'COIS- (.+)', x)
    if match_cois:
        info['conflict_int'] = match_cois.group(1)
        
    match_received_date = re.search(r'PHST- (\d{4}/\d{2}/\d{2} \d{2}:\d{2}) \[received\]', x)
    if match_received_date:
        info['received_date'] = match_received_date.group(1)

    match_accepted_date = re.search(r'PHST- (\d{4}/\d{2}/\d{2} \d{2}:\d{2}) \[accepted\]', x)
    if match_accepted_date:
        info['accepted_date'] = match_accepted_date.group(1)

    match_publication_date = re.search(r'SO  - (.+)', x)
    if match_publication_date:
        info['citation'] = match_publication_date.group(1)
        
    match_dep = re.search(r'DEP - (.+)', x)
    if match_dep:
        info['entry_date'] = match_dep.group(1)

    match_pl = re.search(r'PL  - (.+)', x)
    if match_pl:
        info['pub_place'] = match_pl.group(1)
    
    return info