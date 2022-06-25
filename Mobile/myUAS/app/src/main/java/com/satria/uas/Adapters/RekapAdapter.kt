package com.satria.uas.Adapters

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.satria.uas.Models.RekapModel
import com.satria.uas.R

class RekapAdapter (
    val rekap: ArrayList<RekapModel.Data_masuk>
): RecyclerView.Adapter<RekapAdapter.ViewHolder>(){
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int)=ViewHolder(
        LayoutInflater.from(parent.context)
            .inflate(R.layout.history_list,parent,false)
    )

    override fun onBindViewHolder(holder: RekapAdapter.ViewHolder, position: Int) {
        val history = rekap[position]
        holder.tv_tanggal.text = history.tanggal
        holder.tv_nama.text = history.nama
        holder.tv_email.text = history.email
        holder.tv_hp.text = history.nohp



    }

    override fun getItemCount()=rekap.size
    class ViewHolder(view:View):RecyclerView.ViewHolder(view){
        val tv_tanggal = view.findViewById<TextView>(R.id.tv_tanggal)
        val tv_nama = view.findViewById<TextView>(R.id.tv_nama)
        val tv_email = view.findViewById<TextView>(R.id.tv_email)
        val tv_hp = view.findViewById<TextView>(R.id.tv_hp)

    }
    public fun setData(recapdata : List<RekapModel.Data_masuk>){
        rekap.clear()
        rekap.addAll(recapdata)
        notifyDataSetChanged()
    }

}