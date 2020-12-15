% include('header.tpl', title=name)

% setdefault('error_messages1', [])
% for m in error_messages1:
  <div class="alert alert-danger" role="alert">
    {{m}}
  </div>
% end

<form method="POST" action="/delete" enctype="multipart/form-data">
  <div class="form-group">
    <label for="waehle id">Choose picture to delete</label>
    <input type="number" class="form-control1" id="waehle_id" placeholder="Enter ID" name="id">
   <button type="submit" class="btn btn-primary">Submit</button>
  </div>
</form>

<ul class="nav">
    <li class="nav-item">
        <a class="nav-link active" href="/home">Go to Image Gallery</a>
    </li>

% include('footer.tpl', title=name)
