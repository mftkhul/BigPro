package com.satria.uas.Models

data class RekapModel (
    val data_tamu :List<Data_masuk>
){
    data class Data_masuk(
        val tanggal:String?,
        val nama:String?,
        val email:String?,
        val nohp:String?
    )
}