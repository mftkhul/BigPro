package com.satria.uas.Activities

import android.content.Intent
import android.net.Uri
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.satria.uas.R

class ChatbotActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        supportActionBar?.hide()


        intent = Intent(Intent.ACTION_VIEW)
        intent.setData(Uri.parse("http://192.168.43.187:5000/"))
        startActivity(intent)

    }
}