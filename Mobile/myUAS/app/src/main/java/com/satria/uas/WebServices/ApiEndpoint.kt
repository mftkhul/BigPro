package com.satria.uas.WebServices

import com.satria.uas.Models.RekapModel
import retrofit2.Call
import retrofit2.http.POST

interface ApiEndpoint {
    @POST("data.php")
    fun dataHistoryMasuk(): Call<RekapModel>

}