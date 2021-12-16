#import & linking json with csv
    df = pd.read_json("kode_negara_lengkap.json")
    df_prod = pd.read_csv("produksi_minyak_mentah.csv")
    df_merge = pd.merge(df_prod,df,left_on='kode_negara',right_on='alpha-3')
    
    #sorting
    list_negara = df_merge["name"].unique().tolist()
    list_negara.sort()

    #command control streamlit
    tahun = st.selectbox("Pilih tahun", range(1971, 2016), 44)

    total_produksi = df_merge.groupby(['name', 'kode_negara', 'region', 'sub-region'])['produksi'].sum().reset_index().sort_values(by=['produksi'], ascending=False).reset_index(drop=True)
    total_produksi_max = total_produksi[(total_produksi["produksi"] > 0)].iloc[0]
    total_produksi_min = total_produksi[(total_produksi["produksi"] > 0)].iloc[-1]
    total_produksi_nol = total_produksi[(total_produksi["produksi"] == 0)].sort_values(by=['name']).reset_index(drop=True)
    total_produksi_nol.index += 1

    produksi_tahun = df_merge[(df_merge["tahun"] == tahun)][['name', 'kode_negara', 'region', 'sub-region', 'produksi']].sort_values(by=['produksi'], ascending=False).reset_index(drop=True)
    produksi_tahun_max = produksi_tahun[(produksi_tahun["produksi"] > 0)].iloc[0]
    produksi_tahun_min = produksi_tahun[(produksi_tahun["produksi"] > 0)].iloc[-1]
    produksi_tahun_nol = produksi_tahun[(produksi_tahun["produksi"] == 0)].sort_values(by=['name']).reset_index(drop=True)
    produksi_tahun_nol.index += 1

    
    st.markdown(
        f"""
        #### Negara dengan total produksi keseluruhan tahun terbesar
        Negara: {total_produksi_max["name"]}\n
        Kode negara: {total_produksi_max["kode_negara"]}\n
        Region: {total_produksi_max["region"]}\n
        Sub-region: {total_produksi_max["sub-region"]}\n
        Jumlah produksi: {total_produksi_max["produksi"]}\n
        #### Negara dengan jumlah produksi terbesar pada tahun {tahun}  
        Negara: {produksi_tahun_max["name"]}\n
        Kode negara: {produksi_tahun_max["kode_negara"]}\n
        Region: {produksi_tahun_max["region"]}\n
        Sub-region: {produksi_tahun_max["sub-region"]}\n
        Jumlah produksi: {produksi_tahun_max["produksi"]}\n
        #### Negara dengan total produksi keseluruhan tahun terkecil
        Negara: {total_produksi_min["name"]}\n
        Kode negara: {total_produksi_min["kode_negara"]}\n
        Region: {total_produksi_min["region"]}\n
        Sub-region: {total_produksi_min["sub-region"]}\n
        Jumlah produksi: {total_produksi_min["produksi"]}\n
        #### Negara dengan jumlah produksi terkecil pada tahun {tahun}  
        Negara: {produksi_tahun_min["name"]}\n
        Kode negara: {produksi_tahun_min["kode_negara"]}\n
        Region: {produksi_tahun_min["region"]}\n
        Sub-region: {produksi_tahun_min["sub-region"]}\n
        Jumlah produksi: {produksi_tahun_min["produksi"]}\n
    """
    )
    st.markdown(
        """
        #### Negara dengan total produksi keseluruhan tahun sama dengan nol
        
    """
    )
    total_produksi_nol = total_produksi_nol.drop(['produksi'], axis=1).rename(columns={"name":"Negara", "kode_negara":"Kode Negara", "region":"Region", "sub-region":"Sub Region"})
    st.dataframe(total_produksi_nol)
    st.markdown(
        f"""
        #### Negara dengan jumlah produksi sama dengan nol pada tahun {tahun}
        
    """
    )
    produksi_tahun_nol = produksi_tahun_nol.drop(['produksi'], axis=1).rename(columns={"name":"Negara", "kode_negara":"Kode Negara", "region":"Region", "sub-region":"Sub Region"})
    st.dataframe(produksi_tahun_nol)
