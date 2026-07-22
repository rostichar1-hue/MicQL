cat > install.sh << 'EOF'
#!/bin/bash

echo "🚀 Установка MicroCode..."

# 1. Создаём папку
mkdir -p ~/MicroCode
cd ~/MicroCode

# 2. Копируем файлы (если скачали архив)
cp -r ./* ~/MicroCode/

# 3. Устанавливаем зависимости
pip install tabulate

# 4. Делаем micro исполняемым
chmod +x ~/MicroCode/micro

# 5. Добавляем alias в .bashrc
if ! grep -q "alias micro=" ~/.bashrc; then
    echo 'alias micro="python ~/MicroCode/cli.py"' >> ~/.bashrc
    echo "✅ alias добавлен в .bashrc"
else
    echo "ℹ️ alias уже существует"
fi

# 6. Добавляем в PATH (если нужно)
if [ -d "/data/data/com.termux/files/usr/bin" ]; then
    cp ~/MicroCode/micro /data/data/com.termux/files/usr/bin/
    chmod +x /data/data/com.termux/files/usr/bin/micro
    echo "✅ micro скопирован в /usr/bin/"
fi

echo "🎉 Установка завершена!"
echo "Теперь введи: source ~/.bashrc"
echo "Или перезапусти Termux"
echo "Затем: micro data.mc"
EOF

chmod +x install.sh
