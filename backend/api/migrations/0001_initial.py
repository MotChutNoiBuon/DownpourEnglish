# Generated by Django 5.1.6 on 2025-07-24 13:38

import cloudinary.models
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Tên thành tích')),
                ('description', models.TextField(verbose_name='Mô tả')),
                ('icon', models.CharField(max_length=50, verbose_name='Icon')),
                ('achievement_type', models.CharField(choices=[('learning', 'Học tập'), ('gaming', 'Chơi game'), ('streak', 'Chuỗi ngày'), ('milestone', 'Cột mốc')], max_length=20)),
                ('requirement_value', models.IntegerField(verbose_name='Giá trị yêu cầu')),
                ('points', models.IntegerField(default=10, verbose_name='Điểm thưởng')),
                ('is_active', models.BooleanField(default=True, verbose_name='Đang hoạt động')),
                ('rarity', models.CharField(choices=[('common', 'Thường'), ('uncommon', 'Không thường'), ('rare', 'Hiếm'), ('epic', 'Sử thi'), ('legendary', 'Huyền thoại')], default='common', max_length=20, verbose_name='Độ hiếm')),
            ],
            options={
                'verbose_name': 'Thành tích',
                'verbose_name_plural': 'Thành tích',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Tên chủ đề')),
                ('description', models.TextField(blank=True, verbose_name='Mô tả')),
                ('icon', models.CharField(blank=True, max_length=50, verbose_name='Icon class')),
                ('is_active', models.BooleanField(default=True, verbose_name='Đang hoạt động')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Chủ đề',
                'verbose_name_plural': 'Chủ đề',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('display_name', models.CharField(blank=True, max_length=100, verbose_name='Tên hiển thị')),
                ('avatar', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Avatar')),
                ('total_points', models.IntegerField(default=0, verbose_name='Tổng điểm')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Người dùng',
                'verbose_name_plural': 'Người dùng',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='DailyStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Ngày')),
                ('cards_studied', models.IntegerField(default=0, verbose_name='Số thẻ đã học')),
                ('time_spent', models.IntegerField(default=0, verbose_name='Thời gian học (phút)')),
                ('games_played', models.IntegerField(default=0, verbose_name='Số game đã chơi')),
                ('points_earned', models.IntegerField(default=0, verbose_name='Điểm kiếm được')),
                ('accuracy_rate', models.FloatField(default=0.0, verbose_name='Tỷ lệ chính xác (%)')),
                ('new_words_learned', models.IntegerField(default=0, verbose_name='Từ mới học được')),
                ('words_reviewed', models.IntegerField(default=0, verbose_name='Từ đã ôn tập')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Người dùng')),
            ],
            options={
                'verbose_name': 'Thống kê hàng ngày',
                'verbose_name_plural': 'Thống kê hàng ngày',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='FlashcardSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Tiêu đề')),
                ('description', models.TextField(blank=True, verbose_name='Mô tả')),
                ('is_public', models.BooleanField(default=False, verbose_name='Công khai')),
                ('difficulty', models.CharField(choices=[('beginner', 'Cơ bản'), ('intermediate', 'Trung bình'), ('advanced', 'Nâng cao')], default='beginner', max_length=20)),
                ('total_cards', models.IntegerField(default=0, verbose_name='Tổng số thẻ')),
                ('total_saves', models.IntegerField(default=0, verbose_name='Lượt lưu')),
                ('average_rating', models.FloatField(default=0.0, verbose_name='Điểm trung bình')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Người tạo')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.topic', verbose_name='Chủ đề')),
            ],
            options={
                'verbose_name': 'Bộ flashcard',
                'verbose_name_plural': 'Bộ flashcard',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Flashcard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vietnamese', models.CharField(max_length=500, verbose_name='Tiếng Việt')),
                ('english', models.CharField(max_length=500, verbose_name='Tiếng Anh')),
                ('pronunciation', models.CharField(blank=True, max_length=200, verbose_name='Phiên âm')),
                ('example_sentence_en', models.TextField(blank=True, verbose_name='Câu ví dụ tiếng Anh')),
                ('word_type', models.CharField(blank=True, choices=[('noun', 'Danh từ'), ('verb', 'Động từ'), ('adjective', 'Tính từ'), ('adverb', 'Trạng từ'), ('phrase', 'Cụm từ'), ('other', 'Khác')], max_length=20, verbose_name='Loại từ')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('flashcard_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flashcards', to='api.flashcardset')),
            ],
            options={
                'verbose_name': 'Flashcard',
                'verbose_name_plural': 'Flashcards',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='GameSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_type', models.CharField(choices=[('word_match', 'Ghép từ nhanh'), ('guess_word', 'Đoán từ'), ('crossword', 'Ô chữ')], max_length=20, verbose_name='Loại game')),
                ('score', models.IntegerField(default=0, verbose_name='Điểm số')),
                ('total_questions', models.IntegerField(default=0, verbose_name='Tổng số câu')),
                ('correct_answers', models.IntegerField(default=0, verbose_name='Số câu đúng')),
                ('time_spent', models.IntegerField(default=0, verbose_name='Thời gian (giây)')),
                ('completed_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Người chơi')),
            ],
            options={
                'verbose_name': 'Phiên chơi game',
                'verbose_name_plural': 'Phiên chơi game',
                'ordering': ['-completed_at'],
            },
        ),
        migrations.CreateModel(
            name='SavedFlashcardSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saved_at', models.DateTimeField(auto_now_add=True)),
                ('is_favorite', models.BooleanField(default=False, verbose_name='Yêu thích')),
                ('rating', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Đánh giá (1-5 sao)')),
                ('flashcard_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.flashcardset', verbose_name='Bộ flashcard')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Người dùng')),
            ],
            options={
                'verbose_name': 'Bộ flashcard đã lưu',
                'verbose_name_plural': 'Bộ flashcard đã lưu',
            },
        ),
        migrations.CreateModel(
            name='UserAchievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('earned_at', models.DateTimeField(auto_now_add=True, verbose_name='Đạt được lúc')),
                ('progress_value', models.IntegerField(default=0, verbose_name='Giá trị tiến trình')),
                ('achievement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.achievement', verbose_name='Thành tích')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Người dùng')),
            ],
            options={
                'verbose_name': 'Thành tích người dùng',
                'verbose_name_plural': 'Thành tích người dùng',
                'ordering': ['-earned_at'],
            },
        ),
        migrations.CreateModel(
            name='UserFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, '1 sao - Rất khó'), (2, '2 sao - Khó'), (3, '3 sao - Trung bình'), (4, '4 sao - Dễ'), (5, '5 sao - Rất dễ')], verbose_name='Đánh giá độ khó')),
                ('comment', models.TextField(blank=True, verbose_name='Bình luận')),
                ('is_processed', models.BooleanField(default=False, verbose_name='Đã xử lý')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('flashcard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.flashcard', verbose_name='Flashcard')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Người dùng')),
            ],
            options={
                'verbose_name': 'Phản hồi từ vựng',
                'verbose_name_plural': 'Phản hồi từ vựng',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='UserProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mastery_level', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Mức độ thành thạo (%)')),
                ('times_reviewed', models.IntegerField(default=0, verbose_name='Số lần ôn tập')),
                ('times_correct', models.IntegerField(default=0, verbose_name='Số lần đúng')),
                ('last_reviewed', models.DateTimeField(blank=True, null=True, verbose_name='Lần ôn cuối')),
                ('difficulty_rating', models.IntegerField(blank=True, choices=[(1, 'Rất khó'), (2, 'Khó'), (3, 'Trung bình'), (4, 'Dễ'), (5, 'Rất dễ')], null=True, verbose_name='Đánh giá độ khó')),
                ('is_learned', models.BooleanField(default=False, verbose_name='Đã học')),
                ('is_difficult', models.BooleanField(default=False, verbose_name='Từ khó')),
                ('flashcard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.flashcard', verbose_name='Flashcard')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Người dùng')),
            ],
            options={
                'verbose_name': 'Tiến trình học',
                'verbose_name_plural': 'Tiến trình học',
                'ordering': ['-last_reviewed'],
            },
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['total_points'], name='api_user_total_p_f449a9_idx'),
        ),
        migrations.AddIndex(
            model_name='dailystats',
            index=models.Index(fields=['user', 'date'], name='api_dailyst_user_id_cbe8c6_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='dailystats',
            unique_together={('user', 'date')},
        ),
        migrations.AddIndex(
            model_name='flashcard',
            index=models.Index(fields=['vietnamese'], name='api_flashca_vietnam_ba0af7_idx'),
        ),
        migrations.AddIndex(
            model_name='flashcard',
            index=models.Index(fields=['english'], name='api_flashca_english_bc3c5a_idx'),
        ),
        migrations.AddIndex(
            model_name='gamesession',
            index=models.Index(fields=['user', 'game_type'], name='api_gameses_user_id_8461e5_idx'),
        ),
        migrations.AddIndex(
            model_name='gamesession',
            index=models.Index(fields=['completed_at'], name='api_gameses_complet_8d687c_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='savedflashcardset',
            unique_together={('user', 'flashcard_set')},
        ),
        migrations.AddIndex(
            model_name='flashcardset',
            index=models.Index(fields=['topic', 'difficulty'], name='api_flashca_topic_i_ef267a_idx'),
        ),
        migrations.AddIndex(
            model_name='flashcardset',
            index=models.Index(fields=['is_public', 'created_at'], name='api_flashca_is_publ_a92934_idx'),
        ),
        migrations.AddIndex(
            model_name='flashcardset',
            index=models.Index(fields=['total_saves'], name='api_flashca_total_s_294b98_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='userachievement',
            unique_together={('user', 'achievement')},
        ),
        migrations.AddIndex(
            model_name='userfeedback',
            index=models.Index(fields=['flashcard', 'rating'], name='api_userfee_flashca_c2fd1c_idx'),
        ),
        migrations.AddIndex(
            model_name='userfeedback',
            index=models.Index(fields=['created_at'], name='api_userfee_created_3a264d_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='userfeedback',
            unique_together={('user', 'flashcard')},
        ),
        migrations.AddIndex(
            model_name='userprogress',
            index=models.Index(fields=['user', 'is_difficult'], name='api_userpro_user_id_57f429_idx'),
        ),
        migrations.AddIndex(
            model_name='userprogress',
            index=models.Index(fields=['user', 'mastery_level'], name='api_userpro_user_id_d96fcd_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='userprogress',
            unique_together={('user', 'flashcard')},
        ),
    ]
