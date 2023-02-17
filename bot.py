import telebot,random,requests
from telebot import types
from user_agent import generate_user_agent

coder = input('Enter Token Bot : ')
bot = telebot.TeleBot(coder)
startt = types.InlineKeyboardButton(text='- look ',callback_data='strr')
co = types.InlineKeyboardButton(text='- Developer ',url='t.me/N_P_X')
coder = requests.session()
@bot.message_handler(commands=['start'])
def start(message):
	key = types.InlineKeyboardMarkup()
	key.add(startt)
	key.add(co)
	bot.send_message(message.chat.id,'Welcome To Bot Hunter TikTok 🤓 \n By @N_P_X (3mk) \nlook',reply_markup=key)
	
	

@bot.callback_query_handler(func=lambda call:True)
def qewrew(call):
	if call.data == 'strr':
		startunter(call.message)
		
def startunter(message):
    ok=0
    bad=0
    linktik=0
    while True:
    	num = 'amsoq0winxcnbvzlapaiwyyrmnbvcxz1234567890'
    	user = str(''.join(random.choice(num)for i in range(5)))
    	email = user+'@gmail.com'
    	cardd = types.InlineKeyboardButton(text=f'{email}',callback_data='coder3mk')
    	okk = types.InlineKeyboardButton(text=f'{ok} ✅',callback_data='coder3mk')
    	badd = types.InlineKeyboardButton(text=f'{bad} ❌',callback_data='coder3mk')
    	lockedd = types.InlineKeyboardButton(text=f'{linktik} ⚠️',callback_data='coder3mk')
    	k = types.InlineKeyboardMarkup()
    	k.add(cardd)
    	k.add(okk)
    	k.add(badd)
    	k.add(lockedd)
    	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text='تم التشغيل',reply_markup=k)
    	url = "https://www.tiktok.com/passport/web/user/check_email_registered?shark_extra=%7B%22aid%22%3A1459%2C%22app_name%22%3A%22Tik_Tok_Login%22%2C%22app_language%22%3A%22en%22%2C%22device_platform%22%3A%22web_mobile%22%2C%22region%22%3A%22SA%22%2C%22os%22%3A%22ios%22%2C%22referer%22%3A%22https%3A%2F%2Fwww.tiktok.com%2Fprofile%22%2C%22root_referer%22%3A%22https%3A%2F%2Fwww.google.com%22%2C%22cookie_enabled%22%3Atrue%2C%22screen_width%22%3A390%2C%22screen_height%22%3A844%2C%22browser_language%22%3A%22en-us%22%2C%22browser_platform%22%3A%22iPhone%22%2C%22browser_name%22%3A%22Mozilla%22%2C%22browser_version%22%3A%225.0%20%28iPhone%3B%20CPU%20iPhone%20OS%2014_4%20like%20Mac%20OS%20X%29%20AppleWebKit%2F605.1.15%20%28KHTML%2C%20like%20Gecko%29%20Version%2F14.0.3%20Mobile%2F15E148%20Safari%2F604.1%22%2C%22browser_online%22%3Atrue%2C%22timezone_name%22%3A%22Asia%2FRiyadh%22%2C%22is_page_visible%22%3Atrue%2C%22focus_state%22%3Atrue%2C%22is_fullscreen%22%3Afalse%2C%22history_len%22%3A17%2C%22battery_info%22%3A%7B%7D%7D&msToken=vPgBDLGXZNEf56bl_V4J6muu5nAYCQi5dA6zj49IuWrw2DwDUZELsX2wz2_2ZYtzkbUF9UyblyjQTsIDI5cclvJQ6sZA-lHqzKS1gLIJD9M6LDBgII0nxKqCfwwVstZxhpppXA==&X-Bogus=DFSzsIVLC8A-dJf6SXgssmuyRsO1&_signature=_02B4Z6wo00001dTdX3QAAIDBDn9.7WbolA3U3FvAABfU8c"
    	h = {
    		"User-Agent": generate_user_agent() ,
    }
    	d = f"email={email}&aid=1459&language=en&account_sdk_source=web&region=US"
    	   	
    	r = requests.post(url,headers=h,data=d)
    	if '{"is_registered":1}' in r.text:
    		linktik +=1
    		cook = {
    			'A3': 'd=AQABBCLFxGICENehR8BnUi6pQUzqCTsE5goFEgEBAQEWxmLOYgAAAAAA_eMAAA&S=AQAAAhjVtyai82Rrxg2CK5FMdUc',
    			'A1': 'd=AQABBCLFxGICENehR8BnUi6pQUzqCTsE5goFEgEBAQEWxmLOYgAAAAAA_eMAAA&S=AQAAAhjVtyai82Rrxg2CK5FMdUc',
    			'A1S': 'd=AQABBCLFxGICENehR8BnUi6pQUzqCTsE5goFEgEBAQEWxmLOYgAAAAAA_eMAAA&S=AQAAAhjVtyai82Rrxg2CK5FMdUc&j=WORLD',
    			'AS': 'v=1&s=0sHA17fo&d=A62cb7327|5xRp8pr.2UJmOAqR8uAJglbFObbsH8uOznbuKM00ySlD8Ha.X4jNUXo4VEjGrKs97pN8kPAqzIf1jQcTQp5veb991hp7CXQa18n8eMvtp0i3TKdzY_snYqc41YJj1lVf5YXbOhZFbUgbZ2.BI5VJuQoxc9BfU6gFuHcokkx86DndLRGqMpFyzmFeAViTx6LSbPs2soSDVxJyEtCeBln32VP6QDigRPlUzpL8mrluwSF4NXjjJg3kpS308GYePy96Pznh3CvVja7A0RUIQanRzwQWoKX7u3c5Kgak5jZEasYEQHnqWNCzZXZn5j7BKRKruJ3nhcjBB0BD7YCmViG7NYR1QnbCOntbcWVTvhgr3v7fYIg5cx93ChX3TrMiqfnj.h35U2rNdLWlilATg3BEysTnYSjSIsKcQYnA4C9vzP8Db7tHidwbS1cCjttg.aOyemeymvsE2Y_FsfkK4Qeqx6b0cwqrM7IqzCp0vQp5I_87QmIk8boy4dYeyswIGcdnkLJb45mKMh3DsI5vMN7xyTRhJYO7JVMisaK0Zw8EyrG8z8hCgnozUBv3LpyJjxqbGQGcNBkvn7lhWZgLvsNoBUgVaTEYw5UC0aG7QCh2U7KF9qvv9O0CMZor7aubtx3Z.7SKZVAo7f1yPc4huhhlghkzbNn4BQBL0Fx0dEjQ3Df54gjiOVp5AcJlGM9qlkjbIMDQlg2n_LDedAwQgRoyvPxyrP.Tvqua0OFVi_LUaamtbNsS1SgmJTKobw2K3R39VKy9gcA0vieC9MvgkXQI._E_vz1BtEav0E6RsD2cD.k9j0Jw2brizvfy1wfr6vWoC1bqTMwiEzNGjsX0ug9Yf.yzteWwiWeIAbBG5aSyw9r4O_D9AIig62YIj6y5ERN1msWLRSFv3Dj.ExQ2ek7xuSeN7qW5EIh.4Pnvbm1WNv1TXVuw23WA7HV7WtEiOkfFDs5DvjhLX4MIU_Bt.gpZAcg89Yg-~A|B62cb779f|5f1yTBf.2Tq2W7LQ3KsSFbticESMze16y.0N0bOBd_EFQ_q1.moN9y.T_Vf0mwzJRub.9SzesA7Pzge4dwE_n84Jwg31ipQlUd7uIpky29J0EB2spihP_9ukbwI3MhWdMnds18q42N5ajt9kgn10vdAx5Fp9sNFAbXVl0op1I9bNGrfuz_4_P.a8Eoak702B2ebotX0YdNYct.IJ66Qfd8D.3g1ymlmnHxr7Y2IwJYCg15oQyQBeF8Z7DNW8_kZrP1s6dSZpd75ZI6wro_Rwh2ubvUely.oxpRFUTM2Vlh_VxnvDBDkBPaUC6OO0POVyPIbbCYKUWCVKcMQ_iVYhT.Nh0hntrcppxtz4BVp0rB6jAeb8nc0CrwSFRXP4uo8ICcsK22LsRqH7GWqqpQgrgZC51xJoFGph.Z4ZIX8fMu80u4Eh7lVx4emSGoO3UfrvvkL1RFWxHBfnSxeTmc3dYdPIpJj18qWQShVerqs1UcsB7Hxh67QTx1d2VqqKH9y044pHa55bjeSRnOkIYdHYv2us5rQSEw_04BBRBPAgbSnWrl9COJvpVTVeMF6ykV1.TJzQCKltU4uRTKiQIKfy9vGJuiKjwjFc7h1V5S9Y8Jd69EaDEb1XCaeOAruPYJqc9MINCeycUQFqhxUoHKUORcK9RV_9EINbPwgiB290jhdk3mEffmVI8a8RCcIpiW5dwUCgMkrBb90ebetwP_I9I5fke_USUYS3KtIsOq7L8APsJ4lCmwOdfAPm9OWyLz20bOdk0CidwpDFrqqxQt2JfUe_oyJB8FdZRfmcGmvjrnZm6blzGzUbFnxxJ.5ydhPjmf345BXcxnS3E.U0emkN4Wc0V.xzM_hkQh.oCeqWzSqf15eHZRSoLUusEUA.31Md9l67W_lNcQ.6nASTIWxr_q0l8jjGSGyiyJY-~A',
}

    		headers = {
    			'authority': 'login.yahoo.com',
    			'accept': '*/*',
    			'accept-language': 'en-US,en;q=0.9',
    			'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    			'origin': 'https://login.yahoo.com',
    			'referer': 'https://login.yahoo.com/account/module/create?intl=xa&specId=yidregsimplified&context=reg&done=https%3A%2F%2Fwww.yahoo.com',
    			'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    			'sec-ch-ua-mobile': '?0',
    			'sec-ch-ua-platform': '"Windows"',
    			 'sec-fetch-dest': 'empty',
    			 'sec-fetch-mode': 'cors',
    			 'sec-fetch-site': 'same-origin',
    			 'user-agent': generate_user_agent() ,
    			 'x-requested-with': 'XMLHttpRequest',
}

    		p = {
    			'validateField': 'userId',
}

    		rr = requests.get(f"https://logi.gmail.com/account/module/create").text
    		name = email.split("@gmail.com")[0]
    		data = f'browser-fp-data=%7B%22language%22%3A%22en-US%22%2C%22colorDepth%22%3A24%2C%22deviceMemory%22%3A4%2C%22pixelRatio%22%3A1%2C%22hardwareConcurrency%22%3A4%2C%22timezoneOffset%22%3A420%2C%22timezone%22%3A%22America%2FLos_Angeles%22%2C%22sessionStorage%22%3A1%2C%22localStorage%22%3A1%2C%22indexedDb%22%3A1%2C%22openDatabase%22%3A1%2C%22cpuClass%22%3A%22unknown%22%2C%22platform%22%3A%22Win32%22%2C%22doNotTrack%22%3A%22unknown%22%2C%22plugins%22%3A%7B%22count%22%3A5%2C%22hash%22%3A%222c14024bf8584c3f7f63f24ea490e812%22%7D%2C%22canvas%22%3A%22canvas%20winding%3Ayes~canvas%22%2C%22webgl%22%3A1%2C%22webglVendorAndRenderer%22%3A%22Google%20Inc.%20(Intel)~ANGLE%20(Intel%2C%20Intel(R)%20HD%20Graphics%203000%20Direct3D9Ex%20vs_3_0%20ps_3_0%2C%20igdumd64.dll)%22%2C%22adBlock%22%3A0%2C%22hasLiedLanguages%22%3A0%2C%22hasLiedResolution%22%3A0%2C%22hasLiedOs%22%3A0%2C%22hasLiedBrowser%22%3A0%2C%22touchSupport%22%3A%7B%22points%22%3A0%2C%22event%22%3A0%2C%22start%22%3A0%7D%2C%22fonts%22%3A%7B%22count%22%3A33%2C%22hash%22%3A%22edeefd360161b4bf944ac045e41d0b21%22%7D%2C%22audio%22%3A%22124.04347527516074%22%2C%22resolution%22%3A%7B%22w%22%3A%221600%22%2C%22h%22%3A%22900%22%7D%2C%22availableResolution%22%3A%7B%22w%22%3A%22860%22%2C%22h%22%3A%221600%22%7D%2C%22ts%22%3A%7B%22serve%22%3A1657415199200%2C%22render%22%3A1657415200314%7D%7D&specId=yidregsimplified&cacheStored=&crumb=V0Pr4B6tQHi&acrumb=0sHA17fo&done=https%3A%2F%2Fwww.yahoo.com&googleIdToken=&authCode=&attrSetIndex=0&specData=3qiYX%2FHBcI%2F%2BhrvMxYBXgXQb1%2FYAeMSHZmV4MqgmhqN1URqj%2FsjgTGrzl4FYAaAL1UczLgsaT4rm7Cq3BXusOpCF83nfWay%2BC4rhWCth8rBob6OT8S9v0s7KQfuZoeXmPP0NCJxRHjiKlQBmUepkdKTRtym7LERXeBITKc8qTL15f6Vb9O1yc3ZBETBW%2FOpt6%2FNdXvTgPh8z9rX4CcDlWyjVuO2KusJUgIe2sQ%2BSs7EOIYSCVcNUAOqCtXAFkLyS%2FwtNW9ew2r%2BdkiOEmXXi2Akg3YFs3tNskYHR8cTvqHvpf9mEeGwYDCg0%2FGzQybLfG9um3opaS%2Bvnkz19nTE2jfxnlgudhbhKSkg5b4I3WA7tiQh%2BfdpkINdYrPRYXa%2FbQO47iWX9XnSJm536xRWWqrirGNYme3ZP%2FkbEHdsOCRN59fCXf9GEj0GSdIOYs2OI%2FgcOEl%2BQAV3uH0Dg8OZC0Cm9Nrk%2FYJTIntesxVHvpI5qGAYMr8sR47yrUHuZCahwj9T8tJob%2BJh7cKO1rw83V07K4zwiBSzeQyxbKKj%2BoaUK6tDYVCsS0nsPl9YYzNakW4V6hLVHiMlIwrqdSaaqyD%2FpkWwIZon33c6ulzzRogLES4lZi%2B6Y1I34QbnRs1M1%2Blag9xNYAhe2ysOQWsbec5F2vJaYY941UzlAEH5Z2aoCAgUchjmfRvAqwD3J%2FKlAmwATVMjlgwYwiGZb%2Bc6XIyzGV0P4iq%2F0h8mvJaBqloH%2Be8G%2BOApb2ybaGWor1R1RCt5oHPvbi5pcXhv895j3Pf8R%2BzuCxZu%2F2fLWCugzT4auXfUEvQoR9cBsQxKBe%2Fiw6eo78VzExH9qBh2kpEqtjy1LkHzoh24mn%2FTykqvPMu6cOtu0ZNv%2BCQVEXhER%2BLiZmHqtkvc75fUK1ELu4lKpMitRu4%2BnYTf7saiWOVdn2gQgI2p%2FXU7iPBSxwEzabRpoVwb5wUymGZFsloAcLmBz0FuWtkoqfHzmJdQSZY1y%2BJqMKP30vK8Zy9%2F8RVMpvb859VdesnhF%2B%2B1lFWkfCal3tQNR%2FnN%2BScD4A9rDs1alXxvEpGjnXSpCQ569imLxX11pbaozUXipv4%2BG2WrhGGuTulBoeucBhkiTNf3r73WJfwRCCJCEyztLcYbl3x9P6ahKOjGKEdVDnVi4vGIi47A56jVoQn3QoHmahw6PsqlV4dhtd0u%2BYQ0s09rmFGABQjPdQaSddrB0g32WVOBdruFLeevg9bKRkZYOcr1AfWsuIqi6HaDiKCgomeNN0xB77B0lrwLyS6bW5iGTPP6a%2BlokF6YJKoIlh%2B3xVDWZ4%2Bjj3iEViHGJJA4hsLGy%2FN88eRNZ2RVo957EK3%2FE6vu0L4phnMCwMRxx7PVY2d3oHdGfyMpYFnHK1HRhWspF6PbLoz1jewpUPtuUXmA8qtphATgd4GpwugPQJq6L6n1RFRnHd8WrazHf1HxSO1cZObRYDFPwwR1TK4RkS%2FCoHMePTwNFgy85Z%2FDZ3QYKGhQ8himvoLFH9yLpERLhvS7n%2BV%2BXBJhEOUEDqrTgzf87BX2qI5pKB8P1SZelaAgUU3cXMqxo3et1yxlXaeOptj3K6QrZHs%2BjfTWp5rSVCQ7lj%2BFVql1JChhIU7t0E6h0Y73%2Fy%2BSfnUUtLrjySQQD1vHE%2F6eZYQUHUnz7bYj88EVQZ4e8LAYJvh62gYgoHNIHnk%2Bsa18Q3OUVhcCRqaO4XIiUCWXWaMa8TC7OWOicicC7C73mfEapdQoRpacErL5cDj0lVU%2FkSO31BukbIJ3qXArWnB6xHoBG2L%2FJnwURub4U0e65qB3cAnFe1z%2Bu9SIYRQtmEX%2B%2Fb91mI%2F06XMQd3YrYv%2Bod2sTCVHbpiUXe6vR%2FG5edhHiGB53aMuHX1ljEB711okyoJOViTHu1Fuf4pLhvDSZyOeHBqqX5qj%2FsNjoyZGI1o04O%2F2u%2Bo%2BJMy5YvVVRd8ALRgcpOkqdG9KuT00t1b7R5J5TKKxwUbqMKnkUHGbHi3hA9rHD6Kqn7nfFNvzLmFvA7aN4mFbGy8SncJ9O6MBofHhFnPkhC%2FZdxkYtjDAtSRE9AVNvxEbbGHhqhKBJFaDn%2F2zbK1OqAyC1Wy7rjD7bzYZT3RFKprvz4Dp1SZO732C6%2BcEStFzKt1hK%2FzXDidbZz6bgRhasGBzT2m5ty1F8Y9VCUeIcDbhzkcsztEsqjTbgF1VHJvuxAPo14nDI%2FCHcGCOX7aHSXH4U7G0YFH7O09NruPxcR40KCfO%2FF8eQ%2Bd4ovBGb1SW%2F4wcJ9pWzPKS4XUQ5xSlitdekid5nyDTSEIODfW2vLufF9Da%2BFuj87kH0TtBcM0SR7d5XfYAMA1OOmzOt35LCJGFgF%2F3xyLZv1ghZT%2Bx28qC8fZ7V%2FVnH3uYrVM1S%2FIN71UZRS%2FUK6Cq9bVLrRfGSRqAYlpSalBB8squ%2BsGQ%2FrhLtu6J29Ttg0N1wHovjPX9kPgqsVCcYTIrUE0PcZDw%2BGd5EUiyBNF6HZ4oAMafvj5snS9gLIhIcG82aEhwIfiBR9Rwm%2F%2F7hGq5REIesblFcPIszNvXHr8Prb4xetLLmTYlLxHa9FhoiUG3HxbTJFxSPdc03x9h0665awOppQ4YxAQHjcxOrrzjxhrcZH2TL7DAJZS7F%2FpQae11m00SYVMbufIUT5rCqGf1Kc1zLEbVbEksEgsJ3I3xsjexEUPD9tuDOA5KzqfKBGG3jNbuSrfVcVgk6s9bsGRifmYPbk5ahcXu3c7ekuPG72VDVSaS9kpIFMyVDzQV%2F%2BFdK1vIC48pyZXyVNStS6KxQbKj8CkexdqxJwlV1JpRL8sFYb6o0L%2FMJNL%2B2GMVToSJXCqiM0BaBfvBIae2dIhs2tvZlui7IIUdUAQkwAMjjL9LN%2BvIgdoVtCupTMD3TUqTDfU1Cg0C3K98xi5mfeGP6JJwoSlztXIGDuM4EL%2FnSthWs9gniCkxA36e%2F6zW%2FioH0BKVMFanLjjBRUbaKSdVxtQiJYZ6wiYGJhm%2BTGCPMQG2JLlDj4bJeiNCe8wFzDEDUSL8Q65FLSCcZc9UQBxzSSpeIzCSFT4sY%2Fy61Nr%2BgPgBC36PGOx7M0rPPeeU1ePluevsUiXMhcAl7eayJnr5tG1iqRa%2FFSf5jhEaWM7eC10Ey7iAiNDvtxzoSFRqjnEAADD%2FPzhUmcBJdowhE4Y4YBRB81pIgWFgbuhD31Cnfl93n1UBSPEdvR%2B9acYSeFhLoJFkYIjDzwxi9sjp8ik9wUwk70ff9aJRrkfQRWDliWDaJA2um0X%2FYxazTvk6UYJ9du01kePKT%2BUs8fpulOJhEUi2U02ZyqVwpgeoQmdGrztvt9v7U5vICRNpXm3sdcx8bfkvFMRGsUoxPM%2Fxnla9yal2ZtkWPOltctM%2FmdkJtlBvHjffRBOV9CRHP0b7fIZAGFFh2qQbvkRrf53cQQG3OIM5d5AdtiC7769vQ1uKtciUcAmngVpQfMqXBdSgSA5xG1nKfxyZO9oTGIGlf5xJ9lCdoQdLuyJlR6ma5ro29HzqO%2FelrWrajXYFRMqb0jfbMTZiV0hyZpb8Whu6r5KEQ4i2iyZXrMu%2FKXN1LntbdD8%2BHRBQITCt3hvqkk0D%2BU8e1LGceaHsUyVOKx3KN%2FeH3iUAYX4LhP7QKylegSCMX8ujZMyQarDnJmUhdtdVTpqZuskfC3U%2BFuqcV1ueLwy7i7nwlnJR916wpBEKzJxuu5W4XY1xl295AAkrqQ1w3dQD3Y1RmzbHptQooybc87d4P%2BP48djTkXjk5%2BtzQza31zuVMYeXCEOveFDLjhCWJ%2FEfVo4om0PcaQMJ8rIJcwRPbBCHJHPny%2Bp5IjImeGDscr7NZfj6Rxs9a7BzbRv6sSZitlQrzasw8T5XHIglPVLX9qT1uvUhey%2FETHBTZS%2Fy4CyfIwCBgi7TV4L%2FY0D49DyWNvf9TUP4f%2FxP7fPw0MbUkf16e8fzUE2tkvkeeoYzyXkU5Oe9JSS6c2Jfwo%2FFRTB5K75JNwdog8sebO1NyXRVjJlaoS4SgnVJk5Aix2NUPMcIJU5MmYji0gKu1A6QSODbRtXhmvyd8b1FwRv1MWCSmUHfbkZYxLE6GDO24gaYyrwp0h7ahYC55bti4QrVpPDCcGEj7cUBtzUcLMT2MJOXsfjsAbRsRxBW%2BeMOpMhdnEDTFkNIbUPsmzzrMaUu7Y%2BUAfap639tZUe%2FbNqgibgye2KhlXPS%2FTGtxUGsDZqVBCW03N%2FWahUWhtLKp7KJnutk9otzkZ07VHReV1x3fblTYgS59RSPXwUGY97wQCpSbCFpL7xISbzM0SoAegHDQYy09MtD1vfhfDeEZHyR%2FFCt0YLWvIRVoA8A2K5xWUMmPrd657A2gGKeT0%2FthL%2FZpHTSOLLd5RA9VTKXNVu3xE%2FF0OKQ1HTp4p35M4FJV6eheJOiPgcU1BMuZKMXCXf7x0bpCevEXIeSYaD8pQJHLPXyCj%2BpWzjzNdBhOjbtSdloonEyHvrm19UB10QxDR%2B2fMLKJIDKQJtgYFjQhXGUxGpEmPTQ0uekJZ48ej2Gji1tqWlseMOMipg0S1Rgta7MWQQ3EL88J7u9PJf9soLTOaf7Pqqs%2BobulcEsjxv9aPwILr15ZMfdspWg%2Btx8%2BN5b%2B0uYMSwh%2FOdeMCHS8DONFUKN%2BI8ln3tV0kFaqPNNdHTbwJzbPv1a0Y7v%2FCaqPOoAqXPwpUxmI%2FzgQtCgJ91Raj%2F%2BPNzxDn6JxE7nUIo1X%2BjUwerAkQ2Dygy8Fho%2Bw1BYfihj03CZhjS1krj8Vd04aQabeKSZVzdjfCdpkfzwFHfi77iq6vKPHsQmsZadPFf6aXVazYE6SrXj4RRbaoBsW%2BtJ9PGpu3En9CgvKk9JrArFBq4qRM56H2C%2FwIoUQxYEFQgxiB9RYZMF1ZHmTluTqYOak6GO%2Fw7D%2FZjhBWtnBlpTbMafcrExzCy0YuUklTs5v3gQ6uMdvpWo60FlSd4TBhgRu%2BoyOMzxC2U7swA8JqWlfnvrlX0NmrSYKNHzloPAfpXINg7IR4%2BP2vdHHyEu%2FdymeKI4b3cS8fEDC%2BIr4D%2BfXa1edNyqPdFIFmvKGZeVRDuIXNXM%2BjZLLAD7R8Pw%2FRXC5X%2FgGXX01HU4Ma7vPcIcoUY0HpYRohxZHbuvlCxlbj6MMteOXJJPtgiN7z%2BjC6eyognmaE%2BWWeg4uemCw8mw0Ld2mKorywvWbu4DvOBaXuivqtDfkH5b%2BQstz493hTZ5ovVuAssLygF6US%2FFabYr3KxoyEjmhYpvsA45wctYfcjmFwdf1QT2wQz%2FOoskWn1fCsGKCU6OCb%2BHBCQa5KCSN5y%2FNpOWXUIyB3Z5jQXrs3%2F%2BcWGRkm6fDXJHiASkDuhaJuhg%2BHXaFPTGouoi%2BDpseLIE6QDjIhgVsm2WKIlTJfAekOEQMW8IPzFjABJrdWgZg08BqHIwFTSoMgz6DCT3xP%2BpCZE9xkzXCsPKgtvjqAyVrc8rQWvC2XznQYahjmw%2FTPz10lDVAlH41I8XP132BqPUv5jy3tmjQTFeIkbfH%2BQoe2HN4rHa07AwLHP6Y0gDQqIkbY4lPUoHNPeS6jVXnb6d%2FGFRl8tTKg4QCEaZX3lwzjjXXVAlmz%2BZ0wc1jGXRclTPTNnR%2BvklAjqPIypAz%2BR9tx4rLe5jHLXuCy0LHuIdb5OLrCF%2Fgr1MCywGJHpNao4oeukqk6OPPtFN8eYplJy8tnNwoJSsoNrXR1iNFIt%2F3VZRtgOQvrGQ7x0AXwvVqX6Vt%2BYzQ3WWQdu%2BBI9CsFPE7IX4Ek1ZJ97r1%2BREvommgXkRii4pYbZPEGbkgVMcI42x94LtVEM2ZXqsJyAaQY9rX7bsSAahgp3udxAGzoa%2FjTs6tW1oD6sBin1kcjElZbkBI80DCV2rka9LDImH9ZM7NDDU6leamdb2oJCAmB1YMXozgIV5kpMgbVr1%2BdAPuJX3lKyk9kWI9VrBCtmMo%3D%7CjUP9j77GikcMDQ84gY3nfg%3D%3D%7CIM7sEaFvNp%2BZ6Fsp6b915A%3D%3D&tos0=oath_freereg%7Cxa%7Cen-JO&firstName=&lastName=&userid-domain=yahoo&userId={name}&password=&birthYear=&signup='

    		response = requests.post('https://login.yahoo.com/account/module/create', params=p,cookies=cook,headers=headers, data=data).text
    		if '"userId"' not in response:
    			ok +=1
    			bot.send_message(message.chat.id,f"<strong>New Hunter Account ✅ \n- Username : {name} \n- Email Hunter : {email} \n- By : @N_P_X</strong>",parse_mode='html',reply_markup=key)
    		else:
    			linktik +=1
    			
    	else:
    		bad +=1    		

bot.infinity_polling(True)
