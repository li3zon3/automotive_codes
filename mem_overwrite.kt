package com.example.mem_overwrite

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import java.io.BufferedReader
import java.io.InputStreamReader

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val commandInput = findViewById<EditText>(R.id.command_input)
        val executeButton = findViewById<Button>(R.id.execute_button)
        val resultText = findViewById<TextView>(R.id.result_text)

        executeButton.setOnClickListener {
            val command = commandInput.text.toString()

            try {
                val process = Runtime.getRuntime().exec(command)
                val reader = BufferedReader(InputStreamReader(process.inputStream))
                val errorReader = BufferedReader(InputStreamReader(process.errorStream))
                val output = StringBuilder()
                var line: String?
                while (reader.readLine().also { line = it } != null) {
                    output.append(line).append("\n")
                }
                while (errorReader.readLine().also { line = it } != null) {
                    output.append(line).append("\n")
                }
                resultText.text = output.toString()
            } catch (e: Exception) {
                resultText.text = "Error executing command: ${e.message}\n\n${e.stackTraceToString()}"
            }
        }
    }
}

